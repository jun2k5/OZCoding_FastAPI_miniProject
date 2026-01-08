"""
거래 라우터 (Trade Router)
- 사용자 자산 상태 조회 및 매수/매도 로직 처리
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from auth import get_current_user
import models, schemas
from .market import manager

router = APIRouter()


@router.get("/user/status")
async def get_status(
    current_price: float,
    user: models.User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """자산 상태 조회"""
    # TODO: db.execute와 select를 사용해 유저의 Portfolio 정보를 조회하세요 (변수: result, p)

    # TODO: 포트폴리오 유무에 따라 보유수량(amount)과 평단가(avg_price)를 설정하세요

    # TODO: 현재가 기준 평가금액(evaluation)과 평가손익(profit)을 계산하세요

    # TODO: 다음 키를 가진 딕셔너리를 반환하세요:
    # "cash", "holdings", "evaluation", "profit", "total_asset"
    pass


@router.post("/trade/{action}")
async def trade(
    action: str,
    payload: schemas.TradeRequest,
    user: models.User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """매수 및 매도 처리"""
    # TODO: 유저의 Portfolio 정보를 DB에서 조회하세요 (변수: result, p)

    if action == "buy":
        # TODO: cost(수량*가격) 계산 후 유저 잔액(user.balance) 부족 시 HTTPException 발생

        # TODO: 유저 잔액 차감 및 포트폴리오(p) 업데이트
        # - 기존 데이터(p)가 있으면: 평단가(p.avg_price) 계산 로직 적용 및 수량 증가
        # - 없으면: 새로운 models.Portfolio 객체 생성(new_p) 후 db.add()
        pass

    elif action == "sell":
        # TODO: 포트폴리오 존재 여부와 수량(p.amount) 체크 후 부족 시 HTTPException 발생

        # TODO: 유저 잔액(user.balance) 증가 및 포트폴리오 수량(p.amount) 차감
        # - 수량이 0이 되면 db.delete(p) 실행
        pass

    # TODO: db.flush()로 반영 후 manager.broadcast로 거래 알림을 전송하세요
    # 메시지 형식: {"type": "trade_news", "msg": f"🔔 {user.username}님 {action} 완료"}
    pass
