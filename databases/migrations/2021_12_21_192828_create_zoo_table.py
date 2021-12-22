"""CreateZooTable Migration."""

from masoniteorm.migrations import Migration


class CreateZooTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("zoo") as table:
            table.increments("id")
            table.string("country")
            table.string("animal")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("zoo")
