"""Add a column

Revision ID: 3168880bdb9d
Revises: b708cca102b3
Create Date: 2024-07-06 08:54:32.889067

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3168880bdb9d'
down_revision: Union[str, None] = 'b708cca102b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade() -> None:
    op.drop_column('account', 'last_transaction_date')
