# session.py

# lib
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from contextlib import asynccontextmanager
# pkg



class DatabaseSession:

    def __init__(self) -> None:
        self.action = False
        self.db_url = None
        self.async_engine = None
        self.async_session = None


    def setting(self, config_db):
        self.db_url = config_db["db_url"]
        print( "DB 세팅 완료됨 : ", config_db )


    async def connect(self):
        print( "DB에 연결 중..." )
        self.async_engine = create_async_engine(
            url=self.db_url,
            echo=False,
            pool_size=10
        )
        self.async_session = sessionmaker(
            bind = self.async_engine,
            class_ = AsyncSession,
            expire_on_commit=False
        )
        self.action = True
        print( "DB에 연결 완료 !" )


    async def disconnect(self):
        if self.action == False:
            print( "DB가 기동하지 않았으니 끌수가 없음" )
            return
        
        print( "DB 종료 중..." )
        await self.async_engine.dispose()
        self.async_engine = None
        self.async_session = None
        self.action = False
        print( "DB 종료 완료 !" )


    @asynccontextmanager
    async def get_ss(self):
        print( "get_ss 시작" )
        ss = self.async_session()
        print( type(ss) )
        print( "세션 생성" )
        try:
            yield ss
        finally:
            print( "세션 반환" )
            await ss.close()




DB_SS = DatabaseSession()


