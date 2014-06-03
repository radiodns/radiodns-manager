"""Added shortDescription

Revision ID: 33bc6fe131c7
Revises: 314a9041017e
Create Date: 2014-06-03 17:25:44.348465

"""

# revision identifiers, used by Alembic.
revision = '33bc6fe131c7'
down_revision = '314a9041017e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('station', sa.Column('short_description', sa.String(length=180), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('station', 'short_description')
    ### end Alembic commands ###
