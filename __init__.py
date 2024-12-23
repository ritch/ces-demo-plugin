import fiftyone.operators as foo
import fiftyone.operators.types as types


class CountSamples(foo.Operator):
    @property
    def config(self):
        return foo.OperatorConfig(
            name="count_samples",
            label="Count samples",
            dynamic=True,
        )

    def resolve_input(self, ctx):
        inputs = types.Object()

        if ctx.view != ctx.dataset.view():
            choices = types.RadioGroup()
            choices.add_choice(
                "DATASET",
                label="Dataset",
                description="Count the number of samples in the dataset",
            )

            choices.add_choice(
                "VIEW",
                label="Current view",
                description="Count the number of samples in the current view",
            )

            inputs.enum(
                "target",
                choices.values(),
                required=True,
                default="VIEW",
                view=choices,
            )

        return types.Property(inputs, view=types.View(label="Count samples"))

    def execute(self, ctx):
        print("Executing count_samples")
        target = ctx.params.get("target", "DATASET")
        sample_collection = ctx.view if target == "VIEW" else ctx.dataset
        return {"count": sample_collection.count()}

    def resolve_output(self, ctx):
        target = ctx.params.get("target", "DATASET")
        outputs = types.Object()
        outputs.int(
            "count",
            label=f"Number of samples in the current {target.lower()}",
        )
        return types.Property(outputs)

class HelloWorldPanel(foo.Panel):
    @property
    def config(self):
        return foo.PanelConfig(
            name="hello_world_panel",
            label="Hello World Panel"
        )

    def on_load(self, ctx):
        ctx.panel.state.hello_message = "Hello world!"

    def say_hello(self, ctx):
        ctx.ops.notify(ctx.panel.state.hello_message)

    def render(self, ctx):
        panel = types.Object()
        panel.btn(
            "hello_btn",
            label="Say Hello",
            icon="emoji_people",
            on_click=self.say_hello,
            variant="contained",
        )

        panel_view = types.GridView(
            width=100, height=100, align_x="center", align_y="center"
        )
        return types.Property(panel, view=panel_view)
    

def register(p):
    p.register(CountSamples)
    p.register(HelloWorldPanel)
