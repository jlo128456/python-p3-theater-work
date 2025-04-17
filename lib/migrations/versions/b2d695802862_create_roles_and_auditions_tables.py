"""Create roles and auditions tables

Revision ID: b2d695802862
Revises: 
Create Date: 2025-04-17 23:25:29.291078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2d695802862'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('character_name', sa.String(), nullable=False)
    )

    op.create_table(
        'auditions',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('actor', sa.String(), nullable=False),
        sa.Column('location', sa.String(), nullable=False),
        sa.Column('phone', sa.Integer(), nullable=False),
        sa.Column('hired', sa.Boolean(), default=False),
        sa.Column('role_id', sa.Integer(), sa.ForeignKey('roles.id'))
    )


def downgrade() -> None:
    op.drop_table('auditions')
    op.drop_table('roles')
