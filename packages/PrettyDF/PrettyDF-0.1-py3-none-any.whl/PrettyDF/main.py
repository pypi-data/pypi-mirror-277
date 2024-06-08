def table(dict):
    import pandas as pd
    from tabulate import tabulate

    df = pd.DataFrame(dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))
