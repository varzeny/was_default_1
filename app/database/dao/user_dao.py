# user_dao.py

# lib
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select


# pkg
from app.database.session import DB_SS
from app.database.model.user_model import User


class UserDao:
    def __init__( self ):
        pass


    async def user_create( self, input_user:User, db_ss:AsyncSession=Depends( DB_SS.get_ss ) ):
        db_ss.add( input_user )
        await db_ss.commit()


    async def user_read( self, input_id:str ):
        print("11111")
        async with DB_SS.get_ss() as ss:
            users = await ss.execute(
                select( User ).where( User.id == input_id )
            )
            if users:
                user = users.scalars().first()
                print( "dao 완료" )
                return user
            else:
                print( "dao 완료" )
                return False
            

    async def user_update( self, input_user:User, db_ss:AsyncSession=Depends( DB_SS.get_ss ) ):
        pass


    async def user_delete( self, input_id:str, db_ss:AsyncSession=Depends( DB_SS.get_ss ) ):
        target = await self.user_read_by_id( input_id, db_ss )
        await db_ss.delete( target )
        await db_ss.commit()



USER_DAO = UserDao()