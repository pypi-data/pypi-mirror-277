# -*- coding:utf-8 -*-
"""
Created on 2024/3/28
@author: pei jian
"""
import time

# from xcsc_dataapi import token
from xcsc_dataapi.data import token
from datetime import datetime

if __name__ == "__main__":
    print("当前时间", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    start_time = time.perf_counter()
    pro = token.pro_api('406ea391c34541408f2476de9e864c65')
    # df = pro.query(api_url='/bank/info1', init_date='20240128')
    # df = pro.query(api_url='/tushare/daily')
    # df = pro.query("/stk/api_fm_prd_stk_rstk_lab", stk_cd="000564", affi_begin_date="2018-09-01",
    #                affi_end_date="2018-10-01",
    #                fields="stk_cd,affi_date,lab_date,cir_stk,hldr_name")
    df = pro.query(api_url="/indx/api_fm_prd_indx_quot", trd_strt_date="2024-05-22", trd_end_date="2024-05-22", fields="data_clas,indx_cd,trd_date")

    print(df)
    # 记录结束时间
    end_time = time.perf_counter()
    # 计算执行时间（秒）
    elapsed_time = end_time - start_time
    # 转换为毫秒
    elapsed_time_millis = elapsed_time * 1000
    print(f"执行时间: {elapsed_time_millis:.2f} 毫秒")


