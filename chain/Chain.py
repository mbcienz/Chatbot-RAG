from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnableSerializable

class Chain():
    """Chain is a composable pipeline manager that allows combining multiple
    step into a single executable chain. Each step should implement an `invoke` method 
    (e.g., LangChain Runnable or similar).

    The chain can be built in order of added steps, and executed by calling
    `invoke(prompt)`. This class supports dynamic addition and clearing of steps.
    """
    def __init__(self):
        """chain initialization.
        """
        self.chain_steps = []
        self.chain = None

    def add(self, step):
        """Ensures compatibility with LangChain's Expression Language (LCEL) 
        by automatically wrapping dictionaries into 'RunnableParallel' and 
        callables/methods into 'RunnableLambda'.

        Args:
            step (Any): The step to add. Can be a LangChain Runnable, 
                        a dictionary of runnables, or a callable function/method.
        """
        if isinstance(step, dict):
            # If the step is a dictionary, wrap it into a RunnableParallel 
            # to allow parallel execution of multiple branches.
            step = RunnableParallel(step)
        elif callable(step) and not isinstance(step, (RunnableSerializable, RunnableLambda)):
            # If the step is a callable and not already a LangChain component, 
            # wrap it into a RunnableLambda to make it compatible with the pipe operator.
            step = RunnableLambda(step)
            
        self.chain_steps.append(step)

    def clear(self):
        """reset the current chain
        """
        self.chain_steps = []
        self.chain = None

    def build(self):
        """Build the chain considering the steps in the added order

        Raises:
            ValueError: Raised when trying to build an empty chain.
        """
        if not self.chain_steps:
            raise ValueError("Can not build a chain without steps. Please, add a step.")
        c = self.chain_steps[0]
        for step in self.chain_steps[1:]:
            c = c | step

        self.chain = c

    def invoke(self, prompt):
        """Call the invoke method on the given prompt

        Args:
            prompt (str): Prompt to submit to the model.
        """
        if self.chain is None:
            self.build()
        return self.chain.invoke(prompt)
