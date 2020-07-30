import smbus


class Gyroscope:


    def __init__(self, address, bus = 1):
        self.address = address
        self.bus = smbus.SMBus(bus)

    def reset(self):
        self.bus.write_i2c_block_data(0x6B)
        self.bus.wait_ack()

    def get_acc(self):
      try:
          self.raw_acc_x = self.bus.read_i2c_block_data(self.address, 0x34, 2)
          self.raw_acc_y = self.bus.read_i2c_block_data(self.address, 0x35, 2)
          self.raw_acc_z = self.bus.read_i2c_block_data(self.address, 0x36, 2)
      except IOError:
          print("ReadError: acc")
          return (0, 0, 0)
      else:
            self.k_acc = 16 * 9.81

            self.acc_x = (self.raw_acc_x[1] << 8 | self.raw_acc_x[0]) / 32768 * self.k_acc
            self.acc_y = (self.raw_acc_y[1] << 8 | self.raw_acc_y[0]) / 32768 * self.k_acc
            self.acc_z = (self.raw_acc_z[1] << 8 | self.raw_acc_z[0]) / 32768 * self.k_acc
            if self.acc_x >= self.k_acc:
                self.acc_x -= 2 * self.k_acc

            if self.acc_y >= self.k_acc:
                self.acc_y -= 2 * self.k_acc

            if self.acc_z >= self.k_acc:
                self.acc_z -= 2 * self.k_acc
            return (self.acc_x, self.acc_y, self.acc_z)

    def get_gyro(self):
      try:
            self.raw_gyro_x = self.bus.read_i2c_block_data(self.address, 0x37, 2)
            self.raw_gyro_y = self.bus.read_i2c_block_data(self.address, 0x38, 2)
            self.raw_gyro_z = self.bus.read_i2c_block_data(self.address, 0x39, 2)
      except IOError:
          print("ReadError: gyro")
          return (0, 0, 0)
      else:
            self.k_gyro = 2000
            self.gyro_x = (self.raw_gyro_x[1] << 8 | self.raw_gyro_x[0]) / 32768 * self.k_gyro
            self.gyro_y = (self.raw_gyro_y[1] << 8 | self.raw_gyro_y[0]) / 32768 * self.k_gyro
            self.gyro_z = (self.raw_gyro_z[1] << 8 | self.raw_gyro_z[0]) / 32768 * self.k_gyro

            if self.gyro_x >= self.k_gyro:
                self.gyro_x -= 2 * self.k_gyro

            if self.gyro_y >= self.k_gyro:
                self.gyro_y -= 2 * self.k_gyro

            if self.gyro_z >= self.k_gyro:
                self.gyro_z -= 2 * self.k_gyro

                return (self.gyro_x, self.gyro_y, self.gyro_z)

    def get_angle(self):
      try:
                self.raw_angle_x = self.bus.read_i2c_block_data(self.address, 0x3d, 2)
                self.raw_angle_y = self.bus.read_i2c_block_data(self.address, 0x3e, 2)
                self.raw_angle_z = self.bus.read_i2c_block_data(self.address, 0x3f, 2)
      except IOError:
          print("ReadError: angle")
          return (0, 0, 0)
      else:
            self.k_angle = 180

            self.row = (self.raw_angle_x[1] << 8 | self.raw_angle_x[0]) / 32768 * self.k_angle
            self.pitch = (self.raw_angle_y[1] << 8 | self.raw_angle_y[0]) / 32768 * self.k_angle
            self.yaw = (self.raw_angle_z[1] << 8 | self.raw_angle_z[0]) / 32768 * self.k_angle
            if self.row >= self.k_angle:
                self.row -= 2 * self.k_angle

            if self.pitch >= self.k_angle:
                self.pitch -= 2 * self.k_angle

            if self.yaw >= self.k_angle:
                self.yaw -= 2 * self.k_angle
            return (self.row, self.pitch, self.yaw)

