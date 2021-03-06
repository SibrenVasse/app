"""empty message

Revision ID: 84dec6c29c48
Revises: eef0c404b531
Create Date: 2020-10-21 19:00:43.087487

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84dec6c29c48'
down_revision = 'eef0c404b531'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lifetime_coupon', sa.Column('paid', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lifetime_coupon', 'paid')
    # ### end Alembic commands ###
