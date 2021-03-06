"""empty message

Revision ID: 19c304f256b5
Revises: 3e5b592c6434
Create Date: 2014-09-20 20:04:32.933244

"""

# revision identifiers, used by Alembic.
revision = '19c304f256b5'
down_revision = '3e5b592c6434'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'snapshots')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('snapshots', mysql.VARCHAR(length=256), nullable=True))
    ### end Alembic commands ###
