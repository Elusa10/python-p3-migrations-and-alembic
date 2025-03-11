"""Renaming students to scholars

Revision ID: 84d5d5742bb4
Revises: cb6b78f84299
Create Date: 2025-03-12 00:22:11.778594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84d5d5742bb4'
down_revision = 'cb6b78f84299'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
