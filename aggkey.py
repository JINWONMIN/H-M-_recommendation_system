import pandas as pd
import plotly.express as px

def do_customers_purchase_same_AGGKEY(df, agg_key):
    dfagg = df.groupby(['num_week','customer_id'])[[agg_key]].agg({
            agg_key: lambda x: ','.join(x)
    }).reset_index().rename(columns={agg_key: 'purchased_set'})
    dfagg['num_2wk_before'] = dfagg['num_week'] + 2
    dfagg = pd.merge(
        dfagg[['num_week','customer_id','purchased_set']],
        dfagg.rename(columns={'purchased_set': '2wk_before_purchased_set'})[['num_2wk_before','customer_id','2wk_before_purchased_set']],
        left_on=['num_week', 'customer_id'],
        right_on=['num_2wk_before', 'customer_id'],
        how='left'
    )
    dfagg['num_1wk_before'] = dfagg['num_week'] + 1
    dfagg = pd.merge(
        dfagg,
        dfagg.rename(columns={'purchased_set': '1wk_before_purchased_set'})[['num_1wk_before','customer_id','1wk_before_purchased_set']],
        left_on=['num_week', 'customer_id'],
        right_on=['num_1wk_before', 'customer_id'],
        how='left'
    )
    dfagg['num_3wk_before'] = dfagg['num_week'] + 3
    dfagg = pd.merge(
        dfagg,
        dfagg.rename(columns={'purchased_set': '3wk_before_purchased_set'})[['num_3wk_before','customer_id','3wk_before_purchased_set']],
        left_on=['num_week', 'customer_id'],
        right_on=['num_3wk_before', 'customer_id'],
        how='left'

    )
    dfagg = dfagg[['num_week','customer_id','purchased_set','1wk_before_purchased_set','2wk_before_purchased_set','3wk_before_purchased_set']]
    for col in ['purchased_set','1wk_before_purchased_set', '2wk_before_purchased_set', '3wk_before_purchased_set']:
        dfagg[col] = dfagg[col].fillna('')
        dfagg[col] = dfagg[col].str.split(',')
    dfagg['2wk_before_purchased_set'] = dfagg['2wk_before_purchased_set'] + dfagg['1wk_before_purchased_set']
    dfagg['3wk_before_purchased_set'] = dfagg['3wk_before_purchased_set'] + dfagg['2wk_before_purchased_set']
    for col in ['purchased_set','1wk_before_purchased_set', '2wk_before_purchased_set', '3wk_before_purchased_set']:
        dfagg[col] = dfagg[col].map(set)

    dfagg['is_purchased_same_within_1wk'] = (dfagg['purchased_set'] & dfagg['1wk_before_purchased_set']).astype(int)
    dfagg['is_purchased_same_within_2wk'] = (dfagg['purchased_set'] & dfagg['2wk_before_purchased_set']).astype(int)
    dfagg['is_purchased_same_within_3wk'] = (dfagg['purchased_set'] & dfagg['3wk_before_purchased_set']).astype(int)
    print(
        len(dfagg[dfagg['is_purchased_same_within_3wk'] == 1]['customer_id'].unique()) / len(dfagg['customer_id'].unique()) * 100,
        len(dfagg[dfagg['is_purchased_same_within_2wk'] == 1]['customer_id'].unique()) / len(dfagg['customer_id'].unique()) * 100,
        len(dfagg[dfagg['is_purchased_same_within_1wk'] == 1]['customer_id'].unique()) / len(dfagg['customer_id'].unique()) * 100
    )
    df_vis = pd.DataFrame({
        'Pediod': ['Within_1wk', 'Within_2wk', 'Within_3wk'],
        'Ratio': [len(dfagg[dfagg['is_purchased_same_within_1wk'] == 1]['customer_id'].unique()) / len(dfagg['customer_id'].unique()) * 100,
                  len(dfagg[dfagg['is_purchased_same_within_2wk'] == 1]['customer_id'].unique()) / len(dfagg['customer_id'].unique()) * 100,
                  len(dfagg[dfagg['is_purchased_same_within_3wk'] == 1]['customer_id'].unique()) / len(dfagg['customer_id'].unique()) * 100]
    })
    fig = px.bar(df_vis, x='Pediod', y='Ratio')
    fig.show()
    return dfagg

