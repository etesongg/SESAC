import logging
import argparse

logger = logging.getLogger('my-logger')

# 로그레벨 설정
logging.basicConfig(level=logging.WARNING)

# 로그 포멧팅
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # 2023-08-21 13:42:07,851 - my-logger - WARNING - 헬로우3
hadler = logging.StreamHandler()
# hadler = logging.FileHandler('my-log.log') # type my-log.log 실행
hadler.setFormatter(formatter)
logger.addHandler(hadler)

# 기본 핸들러 제거
logger.propagate = False

# 로그 옵션 동적 처리
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--log-level', choices=['DEBUG', 'INFO', 'WARING', 'ERROR', 'CRITICAL'], default='INFO', help='로그레벨 설정')
args = parser.parse_args()

# 로그 레벨 적용
log_level_args = args.log_level.upper()
logger.setLevel(log_level_args)

# 로그를 출력하는 방법
logger.debug('헬로우5') # 5
logger.info('헬로우4') # 4 level=logging.INFO
logger.warning('헬로우3') # 3 
logger.error('헬로우2') # 2
logger.critical('헬로우1') # 1