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


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('phone_number', sa.String(length=50), nullable=True),
        sa.Column('name', sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
pass


def downgrade() -> None:
    pass
