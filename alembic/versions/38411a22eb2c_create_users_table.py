"""Create users table

Revision ID: 38411a22eb2c
Revises: 1568fd046c65
Create Date: 2024-08-20 18:01:43.696185

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38411a22eb2c'
down_revision: Union[str, None] = '1568fd046c65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
