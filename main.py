import json
import multiprocessing as mp
import threading
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool, Lock

from dnmd_demo import Dnmd
from utils.common import get_conn
from utils.notice_tools import wechat_notice, Email

if __name__ == '__main__':
    111111
    2222222
    conn = get_conn()
    # user_infos = conn.lrange('tt', 0, -1)  # 提取list
    # print(user_infos)
    # user_infos = {

    # }
    # # s = Dnmd()
    # #
    # # for user_info in user_infos:
    # #     inner_info = user_infos[user_info]
    # #     print(inner_info)
    # #     # pool.apply_async(s.login(inner_info.get('id'), inner_info.get('psw')))
    # #     # s.login(inner_info.get('id'), inner_info.get('psw'))
    # #     s.login(**inner_info)
    # #
    user_infos = []
    for key in conn.keys():
        user_infos.append(conn.get(key))
    print(user_infos)
    threads = []
    s = Dnmd(em=Email())

    # for user_info in user_infos:
    #     # inner_info = user_infos[user_info]
    #     # print(inner_info)
    #     inner_info = json.loads(user_info)
    #     print(inner_info)
    #     s.login(**inner_info)
    # 多线程

    for user_info in user_infos:
        # inner_info = user_infos[user_info]
        # print(inner_info)
        inner_info = json.loads(user_info)
        print(inner_info)
        threads.append(threading.Thread(target=s.login, kwargs=inner_info))
    for t in threads:
        t.start()