from rna_browser_lib.rna_plots import RNAplotter
from rna_browser_lib.meta_data_frames import *


def main():

    mouse_shiny = Shiny("mouse")
    print("Loading mouse shiny data")
    mouse_shiny.read_df()

    human_shiny = Shiny("human")
    print("Loading human shiny data")
    human_shiny.read_df()

    both_shiny = Shiny("")
    both_shiny._data = mouse_shiny + human_shiny

    while True:
        while True:
            tissue = str.lower(input(f'Enter a tissue type: "mouse", "human", or "both": ')).strip()
            if tissue == "mouse":
                x = mouse_shiny
                break
            elif tissue == "human":
                x = human_shiny
                break
            elif tissue == "both":
                x = both_shiny
                break
            else:
                print(f'Invalid tissue type: "{tissue}"')

        while True:
            start_date = input("Enter a start date (yymmdd): ").strip()
            if len(start_date) == 6:
                try:
                    start_date = int(start_date)
                    break
                except Exception as e:
                    print(f'Invalid date format: "{start_date}", {e}')
            else:
                print(f'Invalid date format: "{start_date}"')

        while True:
            end_date = input("Enter an end date (yymmdd): ").strip()
            if len(end_date) == 6:
                try:
                    end_date = int(end_date)
                    break
                except Exception as e:
                    print(f'Invalid date format: "{end_date}", {e}')
            else:
                print(f'Invalid date format: "{end_date}"')

        while True:
            tube_prefix = str.upper(input("Enter a tube prefix (P_): ")).strip()
            if sum(x.data()['sample_id'].str[0:2] == tube_prefix) > 0:
                break
            else:
                print(f'No tubes found with prefix {tube_prefix}')

        # Filtering data by tube prefix and patched date range
        all_data = x.data()[x.filter_by_date(start_date, end_date, 'sample_id')]
        user_data = x.data()[x.filter_by_date(start_date, end_date, 'sample_id')
                             & x.filter_by_tube_prefix(tube_prefix)]

        # Making histogram plots
        rna_plotter = RNAplotter()
        rna_plotter.comparison_hist(user_data, all_data, tube_prefix)

        # Asking user if they want to continue making plots
        while True:
            more_plots = str.lower(input("Would you like to continue making plots? (y/n): ")).strip()
            if more_plots == "y":
                break
            elif more_plots == "n":
                exit()
            else:
                print(f'Invalid input: "{more_plots}"')


if __name__ == "__main__":
    main()