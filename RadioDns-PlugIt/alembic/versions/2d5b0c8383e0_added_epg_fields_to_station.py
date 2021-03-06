"""Added EPG fields to Station

Revision ID: 2d5b0c8383e0
Revises: 30a24ab759f9
Create Date: 2014-12-05 12:22:16.897709

"""

# revision identifiers, used by Alembic.
revision = '2d5b0c8383e0'
down_revision = '30a24ab759f9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('station', sa.Column('long_description', sa.String(length=1200), nullable=True))
    op.add_column('station', sa.Column('long_name', sa.String(length=128), nullable=True))
    op.add_column('station', sa.Column('medium_name', sa.String(length=16), nullable=True))
    op.add_column('station', sa.Column('url_default', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('station', 'url_default')
    op.drop_column('station', 'medium_name')
    op.drop_column('station', 'long_name')
    op.drop_column('station', 'long_description')
    ### end Alembic commands ###
