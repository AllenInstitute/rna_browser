import pandas as pd


class MetaDataFrame(object):
    def __init__(self, location: str = "", merge_column: str = ""):
        self._location = location
        self._data = None
        self.merge_column = merge_column

    def read_df(self):
        try:
            self._data = pd.read_csv(self._location, low_memory=False)
        except Exception as e:
            print(f'Invalid filename: {self._location}, {e}')

    def data(self):
        return self._data

    def __mul__(self, other):
        return pd.merge(left=self._data, right=other.data(),
                        left_on=self.merge_column, right_on=other.merge_column, how='inner')

    def __add__(self, other):
        return pd.concat([self._data, other.data()], sort=True)

    def save(self, location: str):
        self._data.to_csv(location, index=None, header=True)


class Shiny(MetaDataFrame):
    def __init__(self, tissue: str):
        if tissue is "mouse":
            super().__init__("//allen/programs/celltypes/workgroups/rnaseqanalysis/shiny/patch_seq/star/"
                             "mouse_patchseq_VISp_current/mapping.df.with.bp.40.lastmap.csv", "cell_name")
        elif tissue is "human":
            super().__init__("//allen\programs/celltypes/workgroups/rnaseqanalysis/shiny/patch_seq/star/"
                             "human/human_patchseq_MTG_current/mapping.df.lastmap.csv", "cell_name")
        else:
            super().__init__("", "cell_name")

    def filter_by_date(self, start_date: int, end_date: int, column_name: str):
        # return self._data[self._data[column_name].str[5:11].astype(int).between(start_date, end_date, inclusive=True)]
        return self._data[column_name].str[5:11].astype(int).between(start_date, end_date, inclusive=True)
        # sample_id, rna_amplification, library_prep

    def filter_by_tube_prefix(self, tube_prefix: str):
        return self._data["sample_id"].str[0:2] == tube_prefix
