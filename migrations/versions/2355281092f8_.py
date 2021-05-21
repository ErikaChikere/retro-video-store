"""empty message

Revision ID: 2355281092f8
Revises: a082fce6dab2
Create Date: 2021-05-20 15:36:26.565876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2355281092f8'
down_revision = 'a082fce6dab2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('videos_checked_out_count', sa.Integer(), nullable=True))
    op.add_column('video', sa.Column('available_inventory', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'available_inventory')
    op.drop_column('customer', 'videos_checked_out_count')
    # ### end Alembic commands ###
