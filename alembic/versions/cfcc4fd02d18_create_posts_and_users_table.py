"""create posts and users table

Revision ID: cfcc4fd02d18
Revises: 
Create Date: 2021-08-29 22:50:42.028498

"""
from alembic import op
import sqlalchemy as sa
from app.routers.database import mydefault_post,mydefault_user

# revision identifiers, used by Alembic.
revision = 'cfcc4fd02d18'
down_revision = None # c'est la base le premier, c'est pour cela pas de down revision
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('post_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )

    # le principe de la démonstration ici est de montrer que l'on peut remplir en plusieurs fois la db:
    #on remplit en pluisieurs fois la table users


    op.create_table('users',
                    sa.Column('user_id', sa.Integer(), nullable=False,default=mydefault_user),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('user_created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('user_id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('posts')
    op.drop_table('users')
    pass
