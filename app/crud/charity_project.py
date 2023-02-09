from typing import Dict, List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(self,
                                     project_name: str,
                                     session: AsyncSession,
                                     ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_charity_project_by_id(self,
                                        project_id: int,
                                        session: AsyncSession,
                                        ) -> Optional[CharityProject]:
        db_project = await session.execute(
            select(CharityProject).where(
                CharityProject.id == project_id
            )
        )
        db_project = db_project.scalars().first()
        return db_project

    async def get_projects_by_completion_rate(self, session: AsyncSession
                                              ) -> Optional[List[Dict[str, str]]]:
        projects = await session.execute(
            select(CharityProject).where(CharityProject.fully_invested)
        )
        projects = projects.scalars().all()
        closed_projects = []
        for proj in projects:
            closed_projects.append({
                'name': proj.name,
                'project_lifetime': proj.close_date - proj.create_date,
                'description': proj.description,
            })
        return sorted(closed_projects, key=lambda i: (i['project_lifetime']))


charity_project_crud = CRUDCharityProject(CharityProject)
