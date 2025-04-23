from app.models.member import Member
from app.dbfactory import Session
from sqlalchemy import insert
from app.dbfactory import SessionLocal

class MemberService():
    @staticmethod
    def member_convert(mdto):
        # 클라이언트에서 전달받은 데이터를 dict형으로 변환
        data = mdto.model_dump()
        mb = Member(**data)
        data = {
            'userid': mb.userid,
            'pwd': mb.pwd,
            'name': mb.name,
            'phone': mb.phone,
            'email': mb.email}

        return data


    @staticmethod
    def insert_member(mdto):
        # 변환된 회원정보를 member 테이블에 저장
        data = MemberService.member_convert(mdto)
        with SessionLocal() as sess:
            stmt = insert(Member).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result


    @staticmethod
    def check_login(userid, pwd):
        with Session() as sess:
            # Member테이블에서 아이디로 회원 조회후
            result = sess.query(Member).filter_by(userid=userid).scalar()
            # 회원이 존재한다면
            # 실제 회원이 존재하고 비밀번호가 일치한다면
            if result and pwd == result.pwd:
                return result
        return None

    @staticmethod
    def selectone_member(userid):
        with Session() as sess:
            result = sess.query(Member).filter_by(userid=userid).scalar()
            return result


    @staticmethod
    def check_userid(userid, db):
        return db.query(Member).filter(Member.userid == userid).first() is not None

    @staticmethod
    def check_phone(phone, db):
        return db.query(Member).filter(Member.phone == phone).first() is not None