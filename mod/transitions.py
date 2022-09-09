import numpy as np

class states():

    def __init__(self, sequence, start_indicator):
        super(states, self).__init__()
        self.ignore = ['None', 'nan', np.nan, None, '']
        self.S = None

        self.t = self.make2d(sequence,start_indicator)
        self.shape = self.t.shape


    def make2d(self,x,start):
        seqs = (x == start).nonzero()[0]
        seqs = [x[start:end] for start, end in list(zip(seqs[:-1], seqs[1:]))+[(seqs[-1], len(x))]]
        # seqs = [np.concatenate([x[start:end], np.array(['END'])]) for start, end in list(zip(seqs[:-1], seqs[1:])) + [(seqs[-1], len(x))]]

        S = [~(k == np.array(self.ignore).reshape(-1,1)).sum(axis=0).astype(bool) for k in seqs]

        seqs = [x[S[i]] for i,x in enumerate(seqs)]
        seqs = [np.concatenate([x[:-1].reshape(-1,1), x[1:].reshape(-1,1)], axis=-1)
                for x in seqs]

        self.S = (~np.concatenate(S)).sum()
        seqs += [np.array([[None,None] for _ in range(self.S)])]


        return np.concatenate(seqs,axis=0)

class metric():

    def __init__(self, hypothetisized_transitions):
        """
        ToDo:
            1. [X] Split conversation up into a segments based on restart message types
            2. [X] Calculate metric per each segment

        Note: The metric here asks how much of a document is described in the happy path. Another
            potential question (which would require reversing some of the summed dimensions) is
            how much of the happy path is followed by the document . . . though you COULD get that
            by simply using the doc to set the hypothesis branches and plugging the ahppy path in as x.

        :param hypothesized_transitions: The hypothesized transitions you expect to see in a document.
        """
        super(metric, self).__init__()
        self.transitions = hypothetisized_transitions


    def search(self, x):
        """
        Note: we can directly compare the input x as a 2d array to the happy path using the following:

            (x == happy_path).astype(int).sum(axis=-1) == 2

        as long as the happy path variable is of shape N_transitions x 1 x 2

        :param x:
        :return:
        """
        comp = np.expand_dims(self.transitions,1)

        return (x == comp).sum(axis=-1) == 2

    def __call__(self, x):
        s = self.search(x).sum(axis=0).astype(bool)
        y = s.mean()
        return y, s