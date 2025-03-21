"""Updated schema

Revision ID: c49e19c13dfb
Revises: 8532de57310b
Create Date: 2025-03-11 11:22:03.149091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c49e19c13dfb'
down_revision: Union[str, None] = '8532de57310b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'author')
    # ### end Alembic commands ###
