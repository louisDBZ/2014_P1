"""add foreign-key to posts table

Revision ID: af786b740296
Revises: 8c82b1632f52
Create Date: 2021-08-29 23:09:52.273247

"""

# pour l'exemple, on ajoute ici user_id et dans la prochaine version, on ajoute le timestamp

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af786b740296'
down_revision = 'cfcc4fd02d18'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'user_id'], remote_cols=['user_id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'user_id') # ici on doit mettre l'équivalent du add / la réciproque
    pass
