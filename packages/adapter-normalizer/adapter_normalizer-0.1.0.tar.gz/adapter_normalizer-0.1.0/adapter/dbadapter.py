from sqlalchemy import update
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from adapter.models.rule import NormalizationRule, StatusType


class DBAdapter:
    def __init__(self, url: str) -> None:
        self.url = url
        engine = create_async_engine(
            url,
            echo=False,
            connect_args={"server_settings": {"jit": "off"}},
        )
        self.async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async def write_rule(
        self,
        model_id: str,
        is_success: bool,
        rule: dict | None = None,
        errors: list[dict] | dict | None = None,
    ):
        values = {
            "status": StatusType.DONE if is_success else StatusType.FAILED,
        }
        if rule and is_success:
            values["mapping"] = rule
        if errors and not is_success:
            values["processing_errors"] = errors

        async with self.async_session_factory() as session:
            stmt = (
                update(NormalizationRule)
                .where(NormalizationRule.model_id == model_id)
                .values(**values)
            )
            await session.execute(stmt)
            await session.commit()
