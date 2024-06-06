import io
from ftplib import FTP, FTP_PORT

from typing import List, Optional

# import httpx

from ....common.logger import logger

# from ....common.storage import BaseStorage
from ....common.types import CrawlerContent
from ..base_plugin import BasePlugin, BaseTag, BaseReader
from ...worker import WorkerTask
from .ftp_dir_listing import DirectoryListing


class FTPReader(BaseReader):
    ftp: FTP
    filepath: str
    filesize: int

    def __init__(self, ftp: FTP, filepath, filesize):
        super().__init__()
        self.ftp = ftp

        # filepath = "/Paintings of the World 3(13 min).mp4"
        # filesize = 461417090

        self.filepath = filepath
        self.filesize = int(filesize)

    def read_to(self, f: io.IOBase):
        cmd = f"RETR {self.filepath}"
        total = 0
        i = 0

        logger.info(f"FTP reading {self.filepath}")

        def write(data):
            nonlocal i, total
            # logger.info(f"writing {len(data)}")
            f.write(data)
            # logger.info("wrote")
            total += len(data)

            if int(total / self.filesize * 100) >= i * 10:
                # if True:
                logger.info(f"FTP read total {total} vs {self.filesize} ({int(total/self.filesize*100)}%)")
                i += 1

        self.ftp.retrbinary(cmd, callback=write)
        logger.info(f"FTP read total {total} ({int(total/self.filesize*100)}%)")


class FTPPlugin(BasePlugin):
    ftp: FTP
    copyright_tags: List[BaseTag]

    def __init__(self, ctx):
        super().__init__(ctx)
        self.copyright_tags = []

    @staticmethod
    def is_supported(url):
        p = BasePlugin.parse_url(url)
        return p.scheme == "ftp"

    @staticmethod
    def parse_ftp_url(url):
        user = "anonymous"
        passwd = ""
        host = ""
        port = int(FTP_PORT)

        p = BasePlugin.parse_url(url)
        netloc = p.netloc
        p = netloc.split("@")
        if len(p) == 1:  # host[:port] only
            p = netloc.split(":")
            host = p[0]
            if len(p) == 2:
                port = int(p[1])
        else:
            # user:passwd
            u = p[0].split(":")
            user = u[0]
            if len(u) == 2:
                passwd = u[1]

            # host[:port]
            p = p[1].split(":")
            host = p[0]
            if len(p) == 2:
                port = int(p[1])
        return (user, passwd, host, port)

    async def process(self, task: WorkerTask):
        # requires FULL url ( with credentials )
        (user, passwd, host, port) = self.parse_ftp_url(task.url)
        self.ftp = FTP()
        self.ftp.connect(host, port)
        self.ftp.login(user, passwd)
        pwd = self.ftp.pwd()
        async for x in self._scan_dir(pwd, 0):
            yield x
        del self.ftp

    async def _scan_dir(self, path, rec):
        # logger.info(f"scanning {path}")
        lister = DirectoryListing()
        self.ftp.dir(path, lister)

        local_copyright_tag = await self._try_find_license(path, lister.contents)
        if len(self.copyright_tags) == 0:
            logger.info(f"no copyright tag in {path}")
            return
        copyright_tag = self.copyright_tags[-1]

        # copyright_tag is pushed to self.copyright_tags

        for item in lister.contents:
            logger.info("\t" * rec + item["permissions"] + "\t" + item["filename"] + "\t" + item["filesize"])
            if DirectoryListing.is_dir(item["permissions"]):
                sub_path = path + item["filename"] + "/"
                async for x in self._scan_dir(sub_path, rec + 1):
                    yield x
            else:
                if item["filename"] == BasePlugin.license_filename:
                    continue

                filepath = f'{path}{item["filename"]}'

                yield CrawlerContent(
                    # tag_id=str(tag) if tag is not None else None,
                    # tag_keepout=tag.is_keepout() if tag is not None else None,
                    copyright_tag_id=str(copyright_tag),
                    copyright_tag_keepout=copyright_tag.is_keepout(),
                    # type=content_type,
                    url=filepath,
                    # content=content,
                    content=FTPReader(self.ftp, filepath, item["filesize"]),
                )
        if local_copyright_tag:
            self.copyright_tags.pop()

    async def _try_find_license(self, path, dir_contents) -> Optional[BaseTag]:
        for item in dir_contents:
            if item["filename"] == BasePlugin.license_filename and not DirectoryListing.is_dir(item["permissions"]):
                logger.info("found license.txt")
                content = await self.download(f'{path}{item["filename"]}')
                if content:
                    logger.info(f"got license content: {content=}")
                    tag = await BasePlugin.parse_tag_in(content.decode())
                    # logger.info(f"{tag_id=}")
                    logger.info(f"{tag=}")
                    if tag:
                        self.copyright_tags.append(tag)
                        return tag
        return None

    async def download(self, path):
        res = b""

        def gather_content(batch):
            nonlocal res
            res += batch

        cmd = f"retr {path}"
        # print(cmd)
        try:
            self.ftp.retrbinary(cmd, gather_content)
            # print(content)
            return res
        except Exception:
            logger.error(f"failed retr {path}")
        return None
