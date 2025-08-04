import asyncio
import time

# 일반(동기) 함수
def sync_func():
  print("동기 함수 시작")
  time.sleep(2)  # 2초간 멈춤
  print("동기 함수 끝")

# 비동기 함수
async def async_func():
  print('비동기 함수 시작')
  await asyncio.sleep(2)   # 2초 기다림, 다른 작업은 계속 가능
  print('비동기 함수 끝')

# 비교 실행
async def main():
  print("▶ 동기 방식:")
  sync_func()
  sync_func()
  print('\n▶ 비동기 방식: ')
  await asyncio.gather(     # 비동기식 실행 2개를 동시에 실행 하게 하려면 await asyncio.gather
      async_func(),
      async_func()
  )

# 실행
asyncio.run(main())
