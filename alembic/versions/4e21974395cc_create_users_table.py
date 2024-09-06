from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

revision = '4e21974395cc'
down_revision = '38411a22eb2c'
branch_labels = None
depends_on = None

def upgrade():
    inspector = Inspector.from_engine(op.get_bind())
    if 'users' not in inspector.get_table_names():
        op.create_table(
            'users',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('email', sa.String(), nullable=False, unique=True),
            sa.Column('hashed_password', sa.String(), nullable=False),
            sa.Column('phone_number', sa.String(), nullable=True, unique=True),
            sa.Column('name', sa.String(), nullable=True)
        )
        op.create_index('ix_users_email', 'users', ['email'], unique=True)
        op.create_index('ix_users_phone_number', 'users', ['phone_number'], unique=True)

def downgrade():
    op.drop_index('ix_users_phone_number', table_name='users')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
