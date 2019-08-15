log_str = """
    2019-07-23 20:36:45,301.301 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 822000/728670 112.8%; Applied: 0; Backlog: 0/1000; Time: 55s(total), 55s(copy); streamer: mysql-bin.001745:409548497; State: migrating; ETA: due\n'
2019-07-23 20:36:45,301.301 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:46,381.381 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 836000/728670 114.7%; Applied: 0; Backlog: 0/1000; Time: 56s(total), 56s(copy); streamer: mysql-bin.001745:432377205; State: migrating; ETA: due\n'
2019-07-23 20:36:46,381.381 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:47,361.361 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 858000/728670 117.7%; Applied: 0; Backlog: 0/1000; Time: 57s(total), 57s(copy); streamer: mysql-bin.001745:451310303; State: migrating; ETA: due\n'
2019-07-23 20:36:47,361.361 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:48,278.278 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 880000/728670 120.8%; Applied: 0; Backlog: 0/1000; Time: 58s(total), 58s(copy); streamer: mysql-bin.001745:470755680; State: migrating; ETA: due\n'
2019-07-23 20:36:48,278.278 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:49,275.275 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 900000/728670 123.5%; Applied: 0; Backlog: 0/1000; Time: 59s(total), 59s(copy); streamer: mysql-bin.001745:490479927; State: migrating; ETA: due\n'
2019-07-23 20:36:49,275.275 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:50,277.277 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 912000/728670 125.2%; Applied: 0; Backlog: 0/1000; Time: 1m0s(total), 1m0s(copy); streamer: mysql-bin.001745:513213546; State: migrating; ETA: due\n'
2019-07-23 20:36:50,278.278 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:50,891.891 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:36:50] [info] binlogsyncer.go:723 rotate to (mysql-bin.001746, 4)\n'
2019-07-23 20:36:50,891.891 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:50,891.891 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:36:50 INFO rotate to next log from mysql-bin.001746:528283275 to mysql-bin.001746\n'
2019-07-23 20:36:50,891.891 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:50,891.891 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:36:50 INFO rotate to next log from mysql-bin.001746:0 to mysql-bin.001746\n'
2019-07-23 20:36:50,891.891 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:50,891.891 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:36:50] [info] binlogsyncer.go:723 rotate to (mysql-bin.001746, 4)\n'
2019-07-23 20:36:50,891.891 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:36:55,322.322 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 964000/728670 132.3%; Applied: 0; Backlog: 0/1000; Time: 1m5s(total), 1m5s(copy); streamer: mysql-bin.001746:102924413; State: migrating; ETA: due\n'
2019-07-23 20:36:55,323.323 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:00,284.284 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1030000/728670 141.4%; Applied: 0; Backlog: 0/1000; Time: 1m10s(total), 1m10s(copy); streamer: mysql-bin.001746:222901715; State: migrating; ETA: due\n'
2019-07-23 20:37:00,284.284 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:05,325.325 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1090000/728670 149.6%; Applied: 0; Backlog: 0/1000; Time: 1m15s(total), 1m15s(copy); streamer: mysql-bin.001746:314587417; State: migrating; ETA: due\n'
2019-07-23 20:37:05,325.325 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,952.952 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Row copy complete\n'
2019-07-23 20:37:09,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,955.955 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1153747/1153747 100.0%; Applied: 0; Backlog: 0/1000; Time: 1m20s(total), 1m19s(copy); streamer: mysql-bin.001746:420879759; State: migrating; ETA: due\n'
2019-07-23 20:37:09,955.955 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,957.957 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Grabbing voluntary lock: gh-ost.164645.lock\n'
2019-07-23 20:37:09,957.957 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,958.958 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Setting LOCK timeout as 6 seconds\n'
2019-07-23 20:37:09,958.958 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,959.959 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Looking for magic cut-over table\n'
2019-07-23 20:37:09,959.959 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,960.960 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Creating magic cut-over table `ytest`.`_sms_batch_log_del`\n'
2019-07-23 20:37:09,960.960 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,965.965 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Magic cut-over table created\n'
2019-07-23 20:37:09,965.965 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,965.965 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Locking `ytest`.`sms_batch_log`, `ytest`.`_sms_batch_log_del`\n'
2019-07-23 20:37:09,965.965 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,966.966 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Tables locked\n'
2019-07-23 20:37:09,966.966 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,966.966 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Session locking original & magic tables is 164645\n'
2019-07-23 20:37:09,966.966 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,966.966 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Writing changelog state: AllEventsUpToLockProcessed:1563885429966627082\n'
2019-07-23 20:37:09,966.966 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,968.968 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Intercepted changelog state AllEventsUpToLockProcessed\n'
2019-07-23 20:37:09,968.968 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,968.968 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Handled changelog state AllEventsUpToLockProcessed\n'
2019-07-23 20:37:09,968.968 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:09,971.971 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:09 INFO Waiting for events up to lock\n'
2019-07-23 20:37:09,971.971 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,274.274 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1153747/1153747 100.0%; Applied: 0; Backlog: 1/1000; Time: 1m20s(total), 1m19s(copy); streamer: mysql-bin.001746:420882367; State: migrating; ETA: due\n'
2019-07-23 20:37:10,274.274 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,952.952 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:10 INFO Waiting for events up to lock: got AllEventsUpToLockProcessed:1563885429966627082\n'
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:10 INFO Done waiting for events up to lock; duration=986.264957ms\n'
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Migrating `ytest`.`sms_batch_log`; Ghost table is `ytest`.`_sms_batch_log_gho`\n'
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Migrating rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306; inspecting rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306; executing on op-ops\n'
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Migration started at Tue Jul 23 20:35:49 +0800 2019\n'
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,953.953 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# chunk-size: 2000; max-lag-millis: 1500ms; dml-batch-size: 50; max-load: Threads_running=30; critical-load: Threads_running=50; nice-ratio: 0.000000\n'
2019-07-23 20:37:10,954.954 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,954.954 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# throttle-additional-flag-file: /tmp/gh-ost.throttle \n'
2019-07-23 20:37:10,954.954 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,954.954 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Serving on unix socket: /www/gh-ost/socket_file/ghost_dba-m_ytest_sms_batch_log_2019-07-23_20:33:43\n'
2019-07-23 20:37:10,954.954 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,955.955 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1153747/1153747 100.0%; Applied: 0; Backlog: 0/1000; Time: 1m21s(total), 1m19s(copy); streamer: mysql-bin.001746:420885521; State: migrating; ETA: due\n'
2019-07-23 20:37:10,955.955 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,958.958 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:10 INFO Setting RENAME timeout as 3 seconds\n'
2019-07-23 20:37:10,958.958 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,958.958 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:10 INFO Session renaming tables is 164647\n'
2019-07-23 20:37:10,958.958 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:10,959.959 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:10 INFO Issuing and expecting this to block: rename /* gh-ost */ table `ytest`.`sms_batch_log` to `ytest`.`_sms_batch_log_del`, `ytest`.`_sms_batch_log_gho` to `ytest`.`sms_batch_log`\n'
2019-07-23 20:37:10,959.959 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,961.961 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b"2019-07-23 20:37:11 INFO Found atomic RENAME to be blocking, as expected. Double checking the lock is still in place (though I don't strictly have to)\n"
2019-07-23 20:37:11,961.961 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,961.961 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:11 INFO Checking session lock: gh-ost.164645.lock\n'
2019-07-23 20:37:11,961.961 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,962.962 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:11 INFO Connection holding lock on original table still exists\n'
2019-07-23 20:37:11,962.962 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,962.962 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:11 INFO Will now proceed to drop magic table and unlock tables\n'
2019-07-23 20:37:11,962.962 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,962.962 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:11 INFO Dropping magic cut-over table\n'
2019-07-23 20:37:11,962.962 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,972.972 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:11 INFO Releasing lock from `ytest`.`sms_batch_log`, `ytest`.`_sms_batch_log_del`\n'
2019-07-23 20:37:11,972.972 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,973.973 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:11 INFO Tables unlocked\n'
2019-07-23 20:37:11,974.974 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,978.978 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:11 INFO Tables renamed\n'
2019-07-23 20:37:11,978.978 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,978.978 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:11 INFO Lock & rename duration: 2.013231153s. During this time, queries on `sms_batch_log` were blocked\n'
2019-07-23 20:37:11,978.978 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,978.978 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:11 INFO Looking for magic cut-over table\n'
2019-07-23 20:37:11,978.978 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:11,980.980 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:11] [info] binlogsyncer.go:164 syncer is closing...\n'
2019-07-23 20:37:11,980.980 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,041.41 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:12] [error] binlogstreamer.go:77 close sync with err: sync is been closing...\n'
2019-07-23 20:37:12,042.42 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,042.42 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Closed streamer connection. err=<nil>\n'
2019-07-23 20:37:12,042.42 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,042.42 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Dropping table `ytest`.`_sms_batch_log_ghc`\n'
2019-07-23 20:37:12,042.42 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,042.42 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:12] [info] binlogsyncer.go:179 syncer is closed\n'
2019-07-23 20:37:12,042.42 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Table dropped\n'
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Am not dropping old table because I want this operation to be as live as possible. If you insist I should do it, please add `--ok-to-drop-table` next time. But I prefer you do not. To drop the old table, issue:\n'
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO -- drop table `ytest`.`_sms_batch_log_del`\n'
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Done migrating `ytest`.`sms_batch_log`\n'
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Removing socket file: /www/gh-ost/socket_file/ghost_dba-m_ytest_sms_batch_log_2019-07-23_20:33:43\n'
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Tearing down inspector\n'
2019-07-23 20:37:12,052.52 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,053.53 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Tearing down applier\n'
2019-07-23 20:37:12,053.53 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,053.53 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Tearing down streamer\n'
2019-07-23 20:37:12,053.53 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,053.53 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Tearing down throttler\n'
2019-07-23 20:37:12,053.53 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,053.53 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Done\n'
2019-07-23 20:37:12,053.53 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,055.55 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b''
2019-07-23 20:37:12,055.55 [file:auto_sql_inception.py function:execute_gh_ost line:677] INFO 执行完成, 开始处理剩余日志
2019-07-23 20:37:12,055.55 [file:auto_sql_inception.py function:execute_gh_ost line:681] INFO 日志处理完成
2019-07-23 20:37:12,055.55 [file:auto_sql_inception.py function:execute_gh_ost line:685] INFO 执行成功
2019-07-23 20:37:12,071.71 [file:auto_sql_inception.py function:execute_gh_ost line:662] INFO 开始执行ghost
2019-07-23 20:37:12,076.76 [file:auto_sql_inception.py function:execute_gh_ost line:671] INFO 开始等待执行结果
2019-07-23 20:37:12,078.78 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO starting gh-ost 1.0.48\n'
2019-07-23 20:37:12,078.78 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,078.78 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Migrating `ytest`.`sms_batch_log`\n'
2019-07-23 20:37:12,078.78 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,090.90 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO connection validated on rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306\n'
2019-07-23 20:37:12,090.90 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,091.91 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO User has REPLICATION CLIENT, REPLICATION SLAVE privileges, and has ALL privileges on `ytest`.*\n'
2019-07-23 20:37:12,091.91 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,093.93 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO binary logs validated on rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306\n'
2019-07-23 20:37:12,093.93 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,093.93 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Inspector initiated on rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306, version 5.6.16-log\n'
2019-07-23 20:37:12,093.93 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,095.95 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Table found. Engine=InnoDB\n'
2019-07-23 20:37:12,095.95 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,117.117 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Estimated number of rows via EXPLAIN: 940897\n'
2019-07-23 20:37:12,117.117 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,121.121 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Master forced to be rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306\n'
2019-07-23 20:37:12,121.121 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,122.122 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO log_slave_updates validated on rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306\n'
2019-07-23 20:37:12,122.122 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,124.124 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO connection validated on rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306\n'
2019-07-23 20:37:12,124.124 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,126.126 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Connecting binlog streamer at mysql-bin.001746:420891059\n'
2019-07-23 20:37:12,126.126 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,126.126 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:12] [info] binlogsyncer.go:133 create BinlogSyncer with config {99999 mysql rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com 3306 admin_m    false false <nil> false UTC true 0 0s 0s 0 false}\n'
2019-07-23 20:37:12,126.126 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,126.126 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:12] [info] binlogsyncer.go:354 begin to sync binlog from position (mysql-bin.001746, 420891059)\n'
2019-07-23 20:37:12,126.126 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,126.126 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:12] [info] binlogsyncer.go:203 register slave for master server rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306\n'
2019-07-23 20:37:12,126.126 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,136.136 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:12] [info] binlogsyncer.go:723 rotate to (mysql-bin.001746, 420891059)\n'
2019-07-23 20:37:12,136.136 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,137.137 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO rotate to next log from mysql-bin.001746:0 to mysql-bin.001746\n'
2019-07-23 20:37:12,137.137 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,137.137 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO connection validated on rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306\n'
2019-07-23 20:37:12,138.138 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,148.148 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO connection validated on rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306\n'
2019-07-23 20:37:12,148.148 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,149.149 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b"2019-07-23 20:37:12 INFO will use time_zone='SYSTEM' on applier\n"
2019-07-23 20:37:12,150.150 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,150.150 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Examining table structure on applier\n'
2019-07-23 20:37:12,150.150 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,151.151 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Applier initiated on rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306, version 5.6.16-log\n'
2019-07-23 20:37:12,151.151 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,151.151 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Dropping table `ytest`.`_sms_batch_log_gho`\n'
2019-07-23 20:37:12,151.151 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,154.154 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Table dropped\n'
2019-07-23 20:37:12,154.154 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,155.155 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Dropping table `ytest`.`_sms_batch_log_del`\n'
2019-07-23 20:37:12,155.155 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,464.464 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Table dropped\n'
2019-07-23 20:37:12,464.464 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,466.466 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Dropping table `ytest`.`_sms_batch_log_ghc`\n'
2019-07-23 20:37:12,466.466 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,468.468 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Table dropped\n'
2019-07-23 20:37:12,468.468 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,468.468 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Creating changelog table `ytest`.`_sms_batch_log_ghc`\n'
2019-07-23 20:37:12,469.469 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,487.487 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Changelog table created\n'
2019-07-23 20:37:12,487.487 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,487.487 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Creating ghost table `ytest`.`_sms_batch_log_gho`\n'
2019-07-23 20:37:12,487.487 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,496.496 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Ghost table created\n'
2019-07-23 20:37:12,496.496 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,496.496 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Altering ghost table `ytest`.`_sms_batch_log_gho`\n'
2019-07-23 20:37:12,496.496 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,558.558 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Ghost table altered\n'
2019-07-23 20:37:12,558.558 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,560.560 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Intercepted changelog state GhostTableMigrated\n'
2019-07-23 20:37:12,560.560 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,574.574 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Waiting for ghost table to be migrated. Current lag is 0s\n'
2019-07-23 20:37:12,574.574 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,574.574 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Handled changelog state GhostTableMigrated\n'
2019-07-23 20:37:12,574.574 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,580.580 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Chosen shared unique key is PRIMARY\n'
2019-07-23 20:37:12,580.580 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,580.580 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Shared columns are id,batch_code,send_type,send_num,send_mobile,content,status,send_result,success_num,task_id,created_at,updated_at,ccc\n'
2019-07-23 20:37:12,580.580 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,583.583 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Listening on unix socket file: /www/gh-ost/socket_file/ghost_dba-m_ytest_sms_batch_log_2019-07-23_20:33:44\n'
2019-07-23 20:37:12,583.583 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,584.584 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Migration min values: [1]\n'
2019-07-23 20:37:12,584.584 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,586.586 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Migration max values: [1153747]\n'
2019-07-23 20:37:12,586.586 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,586.586 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO Waiting for first throttle metrics to be collected\n'
2019-07-23 20:37:12,586.586 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,596.596 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:12 INFO First throttle metrics collected\n'
2019-07-23 20:37:12,596.596 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,596.596 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Migrating `ytest`.`sms_batch_log`; Ghost table is `ytest`.`_sms_batch_log_gho`\n'
2019-07-23 20:37:12,596.596 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,596.596 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Migrating rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306; inspecting rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306; executing on op-ops\n'
2019-07-23 20:37:12,596.596 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,596.596 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Migration started at Tue Jul 23 20:37:12 +0800 2019\n'
2019-07-23 20:37:12,596.596 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,596.596 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# chunk-size: 2000; max-lag-millis: 1500ms; dml-batch-size: 50; max-load: Threads_running=30; critical-load: Threads_running=50; nice-ratio: 0.000000\n'
2019-07-23 20:37:12,597.597 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,597.597 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# throttle-additional-flag-file: /tmp/gh-ost.throttle \n'
2019-07-23 20:37:12,597.597 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,597.597 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Serving on unix socket: /www/gh-ost/socket_file/ghost_dba-m_ytest_sms_batch_log_2019-07-23_20:33:44\n'
2019-07-23 20:37:12,597.597 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:12,599.599 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 0/940897 0.0%; Applied: 0; Backlog: 0/1000; Time: 0s(total), 0s(copy); streamer: mysql-bin.001746:420893429; State: migrating; ETA: N/A\n'
2019-07-23 20:37:12,599.599 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:13,602.602 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 0/940897 0.0%; Applied: 0; Backlog: 0/1000; Time: 1s(total), 1s(copy); streamer: mysql-bin.001746:420897719; State: migrating; ETA: N/A\n'
2019-07-23 20:37:13,602.602 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:14,636.636 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 4000/940897 0.4%; Applied: 0; Backlog: 0/1000; Time: 2s(total), 2s(copy); streamer: mysql-bin.001746:445597873; State: migrating; ETA: N/A\n'
2019-07-23 20:37:14,636.636 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:15,629.629 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 8000/940897 0.9%; Applied: 0; Backlog: 0/1000; Time: 3s(total), 3s(copy); streamer: mysql-bin.001746:469767639; State: migrating; ETA: N/A\n'
2019-07-23 20:37:15,629.629 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:16,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 12000/940897 1.3%; Applied: 0; Backlog: 0/1000; Time: 4s(total), 4s(copy); streamer: mysql-bin.001746:493796731; State: migrating; ETA: 5m9s\n'
2019-07-23 20:37:16,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:17,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 16000/940897 1.7%; Applied: 0; Backlog: 0/1000; Time: 5s(total), 5s(copy); streamer: mysql-bin.001746:517958128; State: migrating; ETA: 4m49s\n'
2019-07-23 20:37:17,618.618 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:17,933.933 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:17] [info] binlogsyncer.go:723 rotate to (mysql-bin.001747, 4)\n'
2019-07-23 20:37:17,933.933 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:17,933.933 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:17 INFO rotate to next log from mysql-bin.001747:529703373 to mysql-bin.001747\n'
2019-07-23 20:37:17,933.933 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:17,934.934 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:17] [info] binlogsyncer.go:723 rotate to (mysql-bin.001747, 4)\n'
2019-07-23 20:37:17,934.934 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:17,934.934 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:17 INFO rotate to next log from mysql-bin.001747:0 to mysql-bin.001747\n'
2019-07-23 20:37:17,934.934 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:18,622.622 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 24000/940897 2.6%; Applied: 0; Backlog: 0/1000; Time: 6s(total), 6s(copy); streamer: mysql-bin.001747:16162488; State: migrating; ETA: 3m49s\n'
2019-07-23 20:37:18,622.622 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:19,629.629 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 44000/940897 4.7%; Applied: 0; Backlog: 0/1000; Time: 7s(total), 7s(copy); streamer: mysql-bin.001747:35747098; State: migrating; ETA: 2m22s\n'
2019-07-23 20:37:19,630.630 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:20,670.670 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 60000/940897 6.4%; Applied: 0; Backlog: 0/1000; Time: 8s(total), 8s(copy); streamer: mysql-bin.001747:57905228; State: migrating; ETA: 1m57s\n'
2019-07-23 20:37:20,670.670 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:21,634.634 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 72000/940897 7.7%; Applied: 0; Backlog: 0/1000; Time: 9s(total), 9s(copy); streamer: mysql-bin.001747:80820977; State: migrating; ETA: 1m48s\n'
2019-07-23 20:37:21,634.634 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:22,612.612 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 82000/940897 8.7%; Applied: 0; Backlog: 0/1000; Time: 10s(total), 10s(copy); streamer: mysql-bin.001747:102700432; State: migrating; ETA: 1m44s\n'
2019-07-23 20:37:22,612.612 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:23,632.632 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 96000/940897 10.2%; Applied: 0; Backlog: 0/1000; Time: 11s(total), 11s(copy); streamer: mysql-bin.001747:125107135; State: migrating; ETA: 1m36s\n'
2019-07-23 20:37:23,632.632 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:24,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 114000/940897 12.1%; Applied: 0; Backlog: 0/1000; Time: 12s(total), 12s(copy); streamer: mysql-bin.001747:142001638; State: migrating; ETA: 1m27s\n'
2019-07-23 20:37:24,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:25,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 130000/940897 13.8%; Applied: 0; Backlog: 0/1000; Time: 13s(total), 13s(copy); streamer: mysql-bin.001747:154041228; State: migrating; ETA: 1m21s\n'
2019-07-23 20:37:25,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:26,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 148000/940897 15.7%; Applied: 0; Backlog: 0/1000; Time: 14s(total), 14s(copy); streamer: mysql-bin.001747:163984099; State: migrating; ETA: 1m15s\n'
2019-07-23 20:37:26,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:27,649.649 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 154000/940897 16.4%; Applied: 0; Backlog: 0/1000; Time: 15s(total), 15s(copy); streamer: mysql-bin.001747:184416600; State: migrating; ETA: 1m16s\n'
2019-07-23 20:37:27,650.650 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:28,646.646 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 174000/940897 18.5%; Applied: 0; Backlog: 0/1000; Time: 16s(total), 16s(copy); streamer: mysql-bin.001747:204162950; State: migrating; ETA: 1m10s\n'
2019-07-23 20:37:28,646.646 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:29,616.616 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 194000/940897 20.6%; Applied: 0; Backlog: 0/1000; Time: 17s(total), 17s(copy); streamer: mysql-bin.001747:224622298; State: migrating; ETA: 1m5s\n'
2019-07-23 20:37:29,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:30,707.707 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 206000/940897 21.9%; Applied: 0; Backlog: 0/1000; Time: 18s(total), 18s(copy); streamer: mysql-bin.001747:244714194; State: migrating; ETA: 1m4s\n'
2019-07-23 20:37:30,707.707 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:31,687.687 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 228000/940897 24.2%; Applied: 0; Backlog: 0/1000; Time: 19s(total), 19s(copy); streamer: mysql-bin.001747:263320012; State: migrating; ETA: 59s\n'
2019-07-23 20:37:31,687.687 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:32,612.612 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 244000/940897 25.9%; Applied: 0; Backlog: 0/1000; Time: 20s(total), 20s(copy); streamer: mysql-bin.001747:285153523; State: migrating; ETA: 57s\n'
2019-07-23 20:37:32,612.612 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:33,712.712 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 258000/940897 27.4%; Applied: 0; Backlog: 0/1000; Time: 21s(total), 21s(copy); streamer: mysql-bin.001747:303420712; State: migrating; ETA: 55s\n'
2019-07-23 20:37:33,713.713 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:34,649.649 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 272000/940897 28.9%; Applied: 0; Backlog: 0/1000; Time: 22s(total), 22s(copy); streamer: mysql-bin.001747:325966983; State: migrating; ETA: 54s\n'
2019-07-23 20:37:34,650.650 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:35,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 290000/940897 30.8%; Applied: 0; Backlog: 0/1000; Time: 23s(total), 23s(copy); streamer: mysql-bin.001747:347265801; State: migrating; ETA: 51s\n'
2019-07-23 20:37:35,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:36,611.611 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 306000/940897 32.5%; Applied: 0; Backlog: 0/1000; Time: 24s(total), 24s(copy); streamer: mysql-bin.001747:369528945; State: migrating; ETA: 49s\n'
2019-07-23 20:37:36,611.611 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:37,610.610 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 316000/940897 33.6%; Applied: 0; Backlog: 0/1000; Time: 25s(total), 25s(copy); streamer: mysql-bin.001747:392445270; State: migrating; ETA: 49s\n'
2019-07-23 20:37:37,611.611 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:38,625.625 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 336000/940897 35.7%; Applied: 0; Backlog: 0/1000; Time: 26s(total), 26s(copy); streamer: mysql-bin.001747:411416782; State: migrating; ETA: 46s\n'
2019-07-23 20:37:38,626.626 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:39,653.653 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 354000/940897 37.6%; Applied: 0; Backlog: 0/1000; Time: 27s(total), 27s(copy); streamer: mysql-bin.001747:430063096; State: migrating; ETA: 44s\n'
2019-07-23 20:37:39,653.653 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:40,706.706 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 362000/940897 38.5%; Applied: 0; Backlog: 0/1000; Time: 28s(total), 28s(copy); streamer: mysql-bin.001747:452296713; State: migrating; ETA: 44s\n'
2019-07-23 20:37:40,706.706 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:41,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 378000/940897 40.2%; Applied: 0; Backlog: 0/1000; Time: 29s(total), 29s(copy); streamer: mysql-bin.001747:473807509; State: migrating; ETA: 43s\n'
2019-07-23 20:37:41,609.609 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:42,634.634 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 392000/940897 41.7%; Applied: 0; Backlog: 0/1000; Time: 30s(total), 30s(copy); streamer: mysql-bin.001747:496872594; State: migrating; ETA: 42s\n'
2019-07-23 20:37:42,634.634 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:43,659.659 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 408000/940897 43.4%; Applied: 0; Backlog: 0/1000; Time: 31s(total), 31s(copy); streamer: mysql-bin.001747:516994048; State: migrating; ETA: 40s\n'
2019-07-23 20:37:43,659.659 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:43,852.852 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:43] [info] binlogsyncer.go:723 rotate to (mysql-bin.001748, 4)\n'
2019-07-23 20:37:43,852.852 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:43,852.852 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:43 INFO rotate to next log from mysql-bin.001748:524358616 to mysql-bin.001748\n'
2019-07-23 20:37:43,852.852 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:43,852.852 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:37:43 INFO rotate to next log from mysql-bin.001748:0 to mysql-bin.001748\n'
2019-07-23 20:37:43,853.853 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:43,853.853 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:37:43] [info] binlogsyncer.go:723 rotate to (mysql-bin.001748, 4)\n'
2019-07-23 20:37:43,853.853 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:44,607.607 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 422000/940897 44.9%; Applied: 0; Backlog: 0/1000; Time: 32s(total), 32s(copy); streamer: mysql-bin.001748:14862112; State: migrating; ETA: 39s\n'
2019-07-23 20:37:44,607.607 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:45,702.702 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 434000/940897 46.1%; Applied: 0; Backlog: 0/1000; Time: 33s(total), 33s(copy); streamer: mysql-bin.001748:37238502; State: migrating; ETA: 38s\n'
2019-07-23 20:37:45,702.702 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:46,610.610 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 440000/940897 46.8%; Applied: 0; Backlog: 0/1000; Time: 34s(total), 34s(copy); streamer: mysql-bin.001748:64687598; State: migrating; ETA: 38s\n'
2019-07-23 20:37:46,610.610 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:47,634.634 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 454000/940897 48.3%; Applied: 0; Backlog: 0/1000; Time: 35s(total), 35s(copy); streamer: mysql-bin.001748:85194932; State: migrating; ETA: 37s\n'
2019-07-23 20:37:47,634.634 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:48,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 466000/940897 49.5%; Applied: 0; Backlog: 0/1000; Time: 36s(total), 36s(copy); streamer: mysql-bin.001748:104482329; State: migrating; ETA: 36s\n'
2019-07-23 20:37:48,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:49,628.628 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 476000/940897 50.6%; Applied: 0; Backlog: 0/1000; Time: 37s(total), 37s(copy); streamer: mysql-bin.001748:126775094; State: migrating; ETA: 36s\n'
2019-07-23 20:37:49,629.629 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:50,637.637 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 498000/940897 52.9%; Applied: 0; Backlog: 0/1000; Time: 38s(total), 38s(copy); streamer: mysql-bin.001748:143092889; State: migrating; ETA: 33s\n'
2019-07-23 20:37:50,637.637 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:51,607.607 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 522000/940897 55.5%; Applied: 0; Backlog: 0/1000; Time: 39s(total), 39s(copy); streamer: mysql-bin.001748:160821119; State: migrating; ETA: 31s\n'
2019-07-23 20:37:51,607.607 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:52,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 540000/940897 57.4%; Applied: 0; Backlog: 0/1000; Time: 40s(total), 40s(copy); streamer: mysql-bin.001748:179354905; State: migrating; ETA: 29s\n'
2019-07-23 20:37:52,605.605 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:53,648.648 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 554000/940897 58.9%; Applied: 0; Backlog: 0/1000; Time: 41s(total), 41s(copy); streamer: mysql-bin.001748:197209242; State: migrating; ETA: 28s\n'
2019-07-23 20:37:53,648.648 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:54,613.613 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 568000/940897 60.4%; Applied: 0; Backlog: 0/1000; Time: 42s(total), 42s(copy); streamer: mysql-bin.001748:221373953; State: migrating; ETA: 27s\n'
2019-07-23 20:37:54,614.614 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:55,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 584000/940897 62.1%; Applied: 0; Backlog: 0/1000; Time: 43s(total), 43s(copy); streamer: mysql-bin.001748:242638482; State: migrating; ETA: 26s\n'
2019-07-23 20:37:55,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:56,678.678 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 604000/940897 64.2%; Applied: 0; Backlog: 0/1000; Time: 44s(total), 44s(copy); streamer: mysql-bin.001748:264184809; State: migrating; ETA: 24s\n'
2019-07-23 20:37:56,683.683 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:57,609.609 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 618000/940897 65.7%; Applied: 0; Backlog: 0/1000; Time: 45s(total), 45s(copy); streamer: mysql-bin.001748:283673703; State: migrating; ETA: 23s\n'
2019-07-23 20:37:57,610.610 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:58,602.602 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 632000/940897 67.2%; Applied: 0; Backlog: 0/1000; Time: 46s(total), 46s(copy); streamer: mysql-bin.001748:306155050; State: migrating; ETA: 22s\n'
2019-07-23 20:37:58,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:37:59,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 646000/940897 68.7%; Applied: 0; Backlog: 0/1000; Time: 47s(total), 47s(copy); streamer: mysql-bin.001748:325336975; State: migrating; ETA: 21s\n'
2019-07-23 20:37:59,605.605 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:00,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 668000/940897 71.0%; Applied: 0; Backlog: 0/1000; Time: 48s(total), 48s(copy); streamer: mysql-bin.001748:342932981; State: migrating; ETA: 19s\n'
2019-07-23 20:38:00,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:01,695.695 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 688000/940897 73.1%; Applied: 0; Backlog: 0/1000; Time: 49s(total), 49s(copy); streamer: mysql-bin.001748:359594127; State: migrating; ETA: 18s\n'
2019-07-23 20:38:01,695.695 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:02,626.626 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 700000/940897 74.4%; Applied: 0; Backlog: 0/1000; Time: 50s(total), 50s(copy); streamer: mysql-bin.001748:371477957; State: migrating; ETA: 17s\n'
2019-07-23 20:38:02,627.627 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:03,615.615 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 714000/940897 75.9%; Applied: 0; Backlog: 0/1000; Time: 51s(total), 51s(copy); streamer: mysql-bin.001748:383147393; State: migrating; ETA: 16s\n'
2019-07-23 20:38:03,615.615 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:04,654.654 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 730000/940897 77.6%; Applied: 0; Backlog: 0/1000; Time: 52s(total), 52s(copy); streamer: mysql-bin.001748:402929371; State: migrating; ETA: 15s\n'
2019-07-23 20:38:04,655.655 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:05,667.667 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 744000/940897 79.1%; Applied: 0; Backlog: 0/1000; Time: 53s(total), 53s(copy); streamer: mysql-bin.001748:422366635; State: migrating; ETA: 14s\n'
2019-07-23 20:38:05,667.667 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:06,632.632 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 754000/940897 80.1%; Applied: 0; Backlog: 0/1000; Time: 54s(total), 54s(copy); streamer: mysql-bin.001748:448034655; State: migrating; ETA: 13s\n'
2019-07-23 20:38:06,632.632 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:07,613.613 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 772000/940897 82.0%; Applied: 0; Backlog: 0/1000; Time: 55s(total), 55s(copy); streamer: mysql-bin.001748:467696142; State: migrating; ETA: 12s\n'
2019-07-23 20:38:07,614.614 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:08,606.606 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 782000/940897 83.1%; Applied: 0; Backlog: 0/1000; Time: 56s(total), 56s(copy); streamer: mysql-bin.001748:488812891; State: migrating; ETA: 11s\n'
2019-07-23 20:38:08,606.606 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:09,602.602 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 802000/940897 85.2%; Applied: 0; Backlog: 0/1000; Time: 57s(total), 57s(copy); streamer: mysql-bin.001748:508120116; State: migrating; ETA: 9s\n'
2019-07-23 20:38:09,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:10,448.448 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:38:10] [info] binlogsyncer.go:723 rotate to (mysql-bin.001749, 4)\n'
2019-07-23 20:38:10,449.449 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:10,449.449 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:10 INFO rotate to next log from mysql-bin.001749:528342410 to mysql-bin.001749\n'
2019-07-23 20:38:10,449.449 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:10,449.449 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:10 INFO rotate to next log from mysql-bin.001749:0 to mysql-bin.001749\n'
2019-07-23 20:38:10,449.449 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:10,449.449 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:38:10] [info] binlogsyncer.go:723 rotate to (mysql-bin.001749, 4)\n'
2019-07-23 20:38:10,449.449 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:10,606.606 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 810000/940897 86.1%; Applied: 0; Backlog: 0/1000; Time: 58s(total), 58s(copy); streamer: mysql-bin.001749:3076364; State: migrating; ETA: 9s\n'
2019-07-23 20:38:10,606.606 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:11,605.605 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 828000/940897 88.0%; Applied: 0; Backlog: 0/1000; Time: 59s(total), 59s(copy); streamer: mysql-bin.001749:22860482; State: migrating; ETA: 8s\n'
2019-07-23 20:38:11,605.605 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:12,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 838000/940897 89.1%; Applied: 0; Backlog: 0/1000; Time: 1m0s(total), 1m0s(copy); streamer: mysql-bin.001749:44603994; State: migrating; ETA: 7s\n'
2019-07-23 20:38:12,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:13,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 860000/940897 91.4%; Applied: 0; Backlog: 0/1000; Time: 1m1s(total), 1m1s(copy); streamer: mysql-bin.001749:62664994; State: migrating; ETA: 5s\n'
2019-07-23 20:38:13,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:14,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 880000/940897 93.5%; Applied: 0; Backlog: 0/1000; Time: 1m2s(total), 1m2s(copy); streamer: mysql-bin.001749:78178282; State: migrating; ETA: 4s\n'
2019-07-23 20:38:14,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:15,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 900000/940897 95.7%; Applied: 0; Backlog: 0/1000; Time: 1m3s(total), 1m3s(copy); streamer: mysql-bin.001749:97902494; State: migrating; ETA: 2s\n'
2019-07-23 20:38:15,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:16,616.616 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 912000/940897 96.9%; Applied: 0; Backlog: 0/1000; Time: 1m4s(total), 1m4s(copy); streamer: mysql-bin.001749:120636091; State: migrating; ETA: 2s\n'
2019-07-23 20:38:16,616.616 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:17,640.640 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 918000/940897 97.6%; Applied: 0; Backlog: 0/1000; Time: 1m5s(total), 1m5s(copy); streamer: mysql-bin.001749:145039481; State: migrating; ETA: 1s\n'
2019-07-23 20:38:17,640.640 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:18,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 932000/940897 99.1%; Applied: 0; Backlog: 0/1000; Time: 1m6s(total), 1m6s(copy); streamer: mysql-bin.001749:165954394; State: migrating; ETA: 0s\n'
2019-07-23 20:38:18,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:22,666.666 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 976000/940897 103.7%; Applied: 0; Backlog: 0/1000; Time: 1m10s(total), 1m10s(copy); streamer: mysql-bin.001749:255752970; State: migrating; ETA: due\n'
2019-07-23 20:38:22,666.666 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:27,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1032000/940897 109.7%; Applied: 0; Backlog: 0/1000; Time: 1m15s(total), 1m15s(copy); streamer: mysql-bin.001749:366890785; State: migrating; ETA: due\n'
2019-07-23 20:38:27,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:32,607.607 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1106000/940897 117.5%; Applied: 0; Backlog: 0/1000; Time: 1m20s(total), 1m20s(copy); streamer: mysql-bin.001749:468078407; State: migrating; ETA: due\n'
2019-07-23 20:38:32,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:35,200.200 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:35 INFO rotate to next log from mysql-bin.001750:524525349 to mysql-bin.001750\n'
2019-07-23 20:38:35,201.201 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:35,201.201 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:38:35] [info] binlogsyncer.go:723 rotate to (mysql-bin.001750, 4)\n'
2019-07-23 20:38:35,201.201 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:35,201.201 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:35 INFO rotate to next log from mysql-bin.001750:0 to mysql-bin.001750\n'
2019-07-23 20:38:35,201.201 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:35,201.201 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:38:35] [info] binlogsyncer.go:723 rotate to (mysql-bin.001750, 4)\n'
2019-07-23 20:38:35,202.202 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,599.599 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Row copy complete\n'
2019-07-23 20:38:36,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,602.602 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1153747/1153747 100.0%; Applied: 0; Backlog: 0/1000; Time: 1m24s(total), 1m24s(copy); streamer: mysql-bin.001750:32044312; State: migrating; ETA: due\n'
2019-07-23 20:38:36,602.602 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,604.604 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Grabbing voluntary lock: gh-ost.165157.lock\n'
2019-07-23 20:38:36,605.605 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,606.606 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Setting LOCK timeout as 6 seconds\n'
2019-07-23 20:38:36,606.606 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,607.607 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Looking for magic cut-over table\n'
2019-07-23 20:38:36,607.607 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Creating magic cut-over table `ytest`.`_sms_batch_log_del`\n'
2019-07-23 20:38:36,608.608 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,641.641 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Magic cut-over table created\n'
2019-07-23 20:38:36,641.641 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,641.641 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Locking `ytest`.`sms_batch_log`, `ytest`.`_sms_batch_log_del`\n'
2019-07-23 20:38:36,641.641 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,642.642 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Tables locked\n'
2019-07-23 20:38:36,642.642 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,642.642 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Session locking original & magic tables is 165157\n'
2019-07-23 20:38:36,642.642 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,643.643 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Writing changelog state: AllEventsUpToLockProcessed:1563885516642606565\n'
2019-07-23 20:38:36,643.643 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,645.645 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Intercepted changelog state AllEventsUpToLockProcessed\n'
2019-07-23 20:38:36,645.645 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,645.645 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Handled changelog state AllEventsUpToLockProcessed\n'
2019-07-23 20:38:36,645.645 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:36,649.649 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:36 INFO Waiting for events up to lock\n'
2019-07-23 20:38:36,649.649 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,599.599 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Waiting for events up to lock: got AllEventsUpToLockProcessed:1563885516642606565\n'
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Done waiting for events up to lock; duration=957.192372ms\n'
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Migrating `ytest`.`sms_batch_log`; Ghost table is `ytest`.`_sms_batch_log_gho`\n'
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Migrating rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306; inspecting rm-bp1106525l5vq06i9150.mysql.rds.aliyuncs.com:3306; executing on op-ops\n'
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Migration started at Tue Jul 23 20:37:12 +0800 2019\n'
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# chunk-size: 2000; max-lag-millis: 1500ms; dml-batch-size: 50; max-load: Threads_running=30; critical-load: Threads_running=50; nice-ratio: 0.000000\n'
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# throttle-additional-flag-file: /tmp/gh-ost.throttle \n'
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Serving on unix socket: /www/gh-ost/socket_file/ghost_dba-m_ytest_sms_batch_log_2019-07-23_20:33:44\n'
2019-07-23 20:38:37,600.600 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1153747/1153747 100.0%; Applied: 0; Backlog: 0/1000; Time: 1m25s(total), 1m24s(copy); streamer: mysql-bin.001750:32049608; State: migrating; ETA: due\n'
2019-07-23 20:38:37,603.603 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,605.605 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Setting RENAME timeout as 3 seconds\n'
2019-07-23 20:38:37,605.605 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,605.605 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Session renaming tables is 165162\n'
2019-07-23 20:38:37,605.605 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,606.606 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Issuing and expecting this to block: rename /* gh-ost */ table `ytest`.`sms_batch_log` to `ytest`.`_sms_batch_log_del`, `ytest`.`_sms_batch_log_gho` to `ytest`.`sms_batch_log`\n'
2019-07-23 20:38:37,606.606 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,611.611 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'Copy: 1153747/1153747 100.0%; Applied: 0; Backlog: 0/1000; Time: 1m25s(total), 1m24s(copy); streamer: mysql-bin.001750:32049608; State: migrating; ETA: due\n'
2019-07-23 20:38:37,611.611 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,616.616 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b"2019-07-23 20:38:37 INFO Found atomic RENAME to be blocking, as expected. Double checking the lock is still in place (though I don't strictly have to)\n"
2019-07-23 20:38:37,616.616 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,616.616 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Checking session lock: gh-ost.165157.lock\n'
2019-07-23 20:38:37,616.616 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Connection holding lock on original table still exists\n'
2019-07-23 20:38:37,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Will now proceed to drop magic table and unlock tables\n'
2019-07-23 20:38:37,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Dropping magic cut-over table\n'
2019-07-23 20:38:37,617.617 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,629.629 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Releasing lock from `ytest`.`sms_batch_log`, `ytest`.`_sms_batch_log_del`\n'
2019-07-23 20:38:37,629.629 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,630.630 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Tables unlocked\n'
2019-07-23 20:38:37,630.630 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,634.634 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Tables renamed\n'
2019-07-23 20:38:37,634.634 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,634.634 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Lock & rename duration: 993.462701ms. During this time, queries on `sms_batch_log` were blocked\n'
2019-07-23 20:38:37,635.635 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,635.635 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Looking for magic cut-over table\n'
2019-07-23 20:38:37,635.635 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,636.636 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:38:37] [info] binlogsyncer.go:164 syncer is closing...\n'
2019-07-23 20:38:37,636.636 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,669.669 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:38:37] [error] binlogstreamer.go:77 close sync with err: sync is been closing...\n'
2019-07-23 20:38:37,669.669 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,669.669 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Closed streamer connection. err=<nil>\n'
2019-07-23 20:38:37,669.669 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,669.669 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Dropping table `ytest`.`_sms_batch_log_ghc`\n'
2019-07-23 20:38:37,669.669 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,669.669 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'[2019/07/23 20:38:37] [info] binlogsyncer.go:179 syncer is closed\n'
2019-07-23 20:38:37,669.669 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Table dropped\n'
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Am not dropping old table because I want this operation to be as live as possible. If you insist I should do it, please add `--ok-to-drop-table` next time. But I prefer you do not. To drop the old table, issue:\n'
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO -- drop table `ytest`.`_sms_batch_log_del`\n'
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Done migrating `ytest`.`sms_batch_log`\n'
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Removing socket file: /www/gh-ost/socket_file/ghost_dba-m_ytest_sms_batch_log_2019-07-23_20:33:44\n'
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Tearing down inspector\n'
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Tearing down applier\n'
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Tearing down streamer\n'
2019-07-23 20:38:37,682.682 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,683.683 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'2019-07-23 20:38:37 INFO Tearing down throttler\n'
2019-07-23 20:38:37,683.683 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,683.683 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b'# Done\n'
2019-07-23 20:38:37,683.683 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:723] INFO 不是进度行
2019-07-23 20:38:37,685.685 [file:auto_sql_inception.py function:handle_gh_ost_log_line line:705] INFO b''
2019-07-23 20:38:37,685.685 [file:auto_sql_inception.py function:execute_gh_ost line:677] INFO 执行完成, 开始处理剩余日志
2019-07-23 20:38:37,685.685 [file:auto_sql_inception.py function:execute_gh_ost line:681] INFO 日志处理完成
2019-07-23 20:38:37,685.685 [file:auto_sql_inception.py function:execute_gh_ost line:685] INFO 执行成功
"""
