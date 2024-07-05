Import("env")

board_config = env.BoardConfig()
board_config.update("build.hwids", [
  ["0x2886", "0x0056"],
  ["0x2886", "0x8056"]
])