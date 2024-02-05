"""First migration

Revision ID: a999183941f0
Revises:
Create Date: 2024-02-03 16:50:33.412064

"""
from typing import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'head'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menus',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('description', sa.Text(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_menus_id'), 'menus', ['id'], unique=False)
    op.create_index(op.f('ix_menus_title'), 'menus', ['title'], unique=False)
    op.create_table('submenus',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('description', sa.Text(), nullable=False),
                    sa.Column('menu_id', sa.UUID(), nullable=True),
                    sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_submenus_id'), 'submenus', ['id'], unique=False)
    op.create_index(op.f('ix_submenus_title'), 'submenus', ['title'], unique=False)
    op.create_table('dishes',
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('description', sa.Text(), nullable=False),
                    sa.Column('price', sa.Numeric(precision=8, scale=2), nullable=False),
                    sa.Column('submenu_id', sa.UUID(), nullable=True),
                    sa.ForeignKeyConstraint(['submenu_id'], ['submenus.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_dishes_id'), 'dishes', ['id'], unique=False)
    op.create_index(op.f('ix_dishes_title'), 'dishes', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dishes_title'), table_name='dishes')
    op.drop_index(op.f('ix_dishes_id'), table_name='dishes')
    op.drop_table('dishes')
    op.drop_index(op.f('ix_submenus_title'), table_name='submenus')
    op.drop_index(op.f('ix_submenus_id'), table_name='submenus')
    op.drop_table('submenus')
    op.drop_index(op.f('ix_menus_title'), table_name='menus')
    op.drop_index(op.f('ix_menus_id'), table_name='menus')
    op.drop_table('menus')
    # ### end Alembic commands ###
