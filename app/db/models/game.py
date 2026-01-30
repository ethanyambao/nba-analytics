from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    game_date: Mapped[date] = mapped_column(Date, nullable=False)

    home_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    away_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)

    home_score: Mapped[int] = mapped_column(Integer, nullable=True)
    away_score: Mapped[int] = mapped_column(Integer, nullable=True)

    status: Mapped[str] = mapped_column(String(50), nullable=False, default="scheduled")
