import requests
import json

# 请求行
url_requests='http://10.17.8.228:9011/payfront/pay-voucher-service/v3/payvoucherbill/front/action/insert'
# 请求头
headers={
    "Content-Type": "application/json",
    "tokenid": "3674246527102a126099253257f47293"
}
# 请求体
requests_data ={
        "appId": "pay_voucher",
        "roleguid": "07B659979B4D49EB88C1E9C07E879C972022_2024420000000_HQ",
        "menuId": "2C27DDF8B6A7688077BA81F9F37EE5EB",
        "actionType": "1",
        "actionName": "新增",
        "glType": "1",
        "params": {
            "accountClsId": "4E72561AB3CD477EB8DFD51813EC2FB2",
            "accountType": "63",
            "isFinancial": "0",
            "batchUserEleType": "1",
            "enableRelation": "false",
            "relations": "gov_bgt_eco;dep_bgt_eco;set_mode;fund_traobj_type",
            "showContact": "false",
            "contactType": "0"
        },
        "datas": [
            {
                "budget_level_code": "1",
                "bgt_mof_dep": "29政法处",
                "found_type_code": "212",
                "agency_code": "331113",
                "canuse_amt": 210000,
                "dis_amt": 0,
                "found_type": "212-上级结算",
                "bgt_mof_dep_name": "政法处",
                "bgt_exe_flag_code": "1",
                "sup_bgt_doc_no": "财行〔2023〕287号",
                "zdzjjqpt": "2-否",
                "sumguid": "1742372609479389184",
                "manage_mof_dep": "29-政法处",
                "pay_type_code": "1",
                "bgt_type_code": "21",
                "fiscal_year": "2024",
                "gov_bgt_eco": "",
                "distri_type_name": "因素法",
                "is_more_pay": "2",
                "planuseamt": 55264,
                "bill_id": "DEB98E9D4D7B76DB8C810E5FE6D5623D",
                "mof_div_code": "420000000",
                "direct_flag": "09-其他",
                "source_type": "4-预算调剂",
                "version": "2024-01-03 09:07:40",
                "budget_level": "1-中央级",
                "zdzjjqpt_name": "否",
                "exp_func_name": "监狱业务及罪犯改造",
                "pro_name": "蔡甸GZ费",
                "lzfs_code": "001",
                "aviamt": 210000,
                "fund_type": "11111-经费拨款补助",
                "ori_bgt_batch_no": "其他",
                "gov_bgt_eco_code": "50201",
                "canuseamt": 210000,
                "update_time": "2024-01-03 09:07:40",
                "bgt_source_code": "1",
                "ccid": "7d2a8980130995c4d812af406e29c384",
                "fromctrl_id": "23585956",
                "exp_func_code": "2040705",
                "ori_fiscal_id": "99",
                "income_sort_name": "公共安全共同财政事权转移支付收入",
                "distri_type_code": "1",
                "agency_name": "湖北省蔡甸监狱",
                "agency": "331113-湖北省蔡甸监狱",
                "frozenamt": 0,
                "fund_type_name": "经费拨款补助",
                "cur_amt": 0,
                "bgt_mof_dep_code": "29",
                "cor_bgt_doc_no": "鄂财政发〔2023〕18号",
                "pro_cat_code": "313",
                "bgt_type_name": "当年预算",
                "pay_type_name": "国库集中支付",
                "manage_mof_dep_name": "政法处",
                "dep_bgt_eco_name": "电费",
                "toctrl_id": "23599390",
                "zdzjjqpt_code": "2",
                "is_not_control_pay": "2",
                "clear_amt": 0,
                "plan_caliber_id": "cbea6259f78839701b66fd4cadc1ed50",
                "bgt_id": "DEB98E9D4D7B76DB8C810E5FE6D5623D",
                "pay_caliber_id": "DEB98E9D4D7B76DB8C810E5FE6D5623D",
                "xpay_amt": 0,
                "is_scientific_code": "2",
                "pay_amt": 3,
                "create_time": "2024-01-03 09:07:40",
                "found_type_name": "上级结算",
                "budget_level_name": "中央级",
                "planaviamt": 565000,
                "threesafe_symbolcat": "000-非“三保”支出",
                "pro": "42000022331T000000239-蔡甸GZ费",
                "is_manager": "2",
                "bgt_exe_flag_name": "可执行",
                "is_gov_pur_code": "2",
                "dep_bgt_eco": "undefined##30206##电费",
                "creater": "F64EE53BCB184E23ACA2E59ACF6710C2",
                "bgt_doc_title": "省财政厅关于提前下达2024年中央监狱补助资金的通知",
                "threesafe_symbolcat_name": "非“三保”支出",
                "fund_type_code": "11111",
                "income_sort_code": "1100244",
                "useamt": 0,
                "source_type_name": "预算调剂",
                "is_contrlbyplan": "2",
                "updater": "F64EE53BCB184E23ACA2E59ACF6710C2",
                "pro_cat": "313-一次性项目",
                "is_deleted": 2,
                "source_type_code": "4",
                "manage_mof_dep_code": "29",
                "is_gov_pur_name": "否",
                "threesafe_symbolcat_code": "000",
                "pro_cat_name": "一次性项目",
                "bill_type_code": "191",
                "pay_type": "1-国库集中支付",
                "hold8_name": "2",
                "pro_code": "42000022331T000000239",
                "amount": 210000,
                "is_pural": "2",
                "bgt_dec": "省财政厅关于提前下达2024年中央监狱补助资金的通知",
                "is_end": "0",
                "exp_func": "2040705-监狱业务及罪犯改造",
                "dep_bgt_eco_code": "30206",
                "gov_bgt_eco_name": "办公经费",
                "plancanuseamt": 509736,
                "agency_acct_name": "",
                "agency_acct_no": "",
                "pay_bank_name": "中国银行股份有限公司武汉蔡甸支行",
                "social_credit_code": "",
                "pay_acct_name": "湖北省蔡甸监狱",
                "payee_acct_name": "蔡必刚",
                "pay_acct_no": "557372255867",
                "payee_acct_no": "6228483268311595979",
                "pay_acct_bank_name": "中国银行股份有限公司武汉蔡甸支行",
                "payee_acct_bank_name": "农行仙桃支行",
                "payee_acct_code": "",
                "fund_traobj_type": "576DE01E1B3326464E6B75DE8984BD2C##11##与部门外同级政府单位",
                "fund_traobj_type_id": "576DE01E1B3326464E6B75DE8984BD2C",
                "fund_traobj_type_code": "11",
                "fund_traobj_type_name": "与部门外同级政府单位",
                "internal_dep": "FAE21E8A74794B1C9B8EFA0244C83DF8##02##刑罚执行科",
                "internal_dep_id": "FAE21E8A74794B1C9B8EFA0244C83DF8",
                "internal_dep_code": "02",
                "internal_dep_name": "刑罚执行科",
                "set_mode": "F522AB99C43B9A2A4DD4C30CB75B50C7##1##电子转账支付",
                "set_mode_id": "F522AB99C43B9A2A4DD4C30CB75B50C7",
                "set_mode_code": "1",
                "set_mode_name": "电子转账支付",
                "use_des": "今天",
                "pay_app_amt": 3,
                "pay_app_amt_big": "贰元整",
                "contract_no": "",
                "acc_type_id": "D3828BFDBF8EE69B76117257F5C6QXC3",
                "acc_type_code": "21",
                "acc_type_name": "单位零余额账户",
                "is_advancefunds": "2",
                "pay_acct_id": "228E5F059256473989F8EEB5B48AB73A",
                "pay_acct_code": "331113",
                "pay_bank_id": "A520EA13DE3A4D078352B4617C0E39B2",
                "pay_bank_code": "104521004371",
                "attachment_id": "",
                "plan_balance_id": "1742372609479389184",
                "fileList": [],
                "ext": {
                    "is_advancefunds": "2",
                    "is_pural": "0"
                }
            }
        ]
    }

# 请求头为json格式时，需要将date的类型转换，使用json.dumps
requests_data1=json.dumps(requests_data)
# print(type(requests_data))
# print(type(requests_data1))


# 发起请求（url,data=bady）
req_data = requests.post(url_requests,data=requests_data1,headers=headers)
# 响应体转json格式
response = req_data.json()
# 打印响应体数据
# #print(req_login.text)
print(response)
# 将响应体以json格式美化
json_str=json.dumps(response,ensure_ascii=False,indent=4)
# 打印美化
print(json_str)