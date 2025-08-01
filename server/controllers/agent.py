from http import HTTPStatus
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from database import get_db
from database.models import Agent
from schemas.agent_schema import AgentCreate, AgentResponse
from schemas.response_schema import ResponseSchema
from sqlalchemy.ext.asyncio import AsyncSession

from utils.auth import get_current_user


router = APIRouter()

@router.post("/agent/register", response_model=ResponseSchema[AgentResponse])
async def register_agent(
    agent_data:AgentCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_agent = Agent(
        user_id=current_user.id,
        hostname=agent_data.hostname,
        os=agent_data.os
    )
    db.add(new_agent)
    await db.commit()
    await db.refresh(new_agent)
    
    return ResponseSchema(
        status=HTTPStatus.CREATED.value,
        message="Agent registered successfully",
        data=new_agent
    )

@router.get("/agent/all", response_model=ResponseSchema[list[AgentResponse]])
async def list_agents(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    result = await db.execute(select(Agent).where(Agent.user_id == current_user.id))
    agents = result.scalars().all()
    return ResponseSchema(
        status=HTTPStatus.OK.value,
        message="Agents fetched",
        data=agents
    )

@router.delete("/agent/{agent_id}", response_model=ResponseSchema[None])
async def delete_agent(
    agent_id: UUID,
    db:AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    result = await db.execute(select(Agent).where(Agent.id == agent_id, Agent.user_id == current_user.id))
    agent = result.scalar_one_or_none()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    await db.delete(agent)
    await db.commit()

    return ResponseSchema(
        status=HTTPStatus.OK.value,
        message="Agent deleted successfully",
        data=None
    )

@router.put("/agent/{agent_id}", response_model=ResponseSchema[AgentResponse])
async def update_agent(
    agent_id: UUID,
    agent_data: AgentCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    result = await db.execute(select(Agent).where(Agent.id == agent_id, Agent.user_id == current_user.id))
    agent = result.scalar_one_or_none()

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent.hostname = agent_data.hostname
    agent.os = agent_data.os

    await db.commit()
    await db.refresh(agent)

    return ResponseSchema(
        status=str(HTTPStatus.OK.value),
        message="Agent updated successfully",
        data=agent
    )