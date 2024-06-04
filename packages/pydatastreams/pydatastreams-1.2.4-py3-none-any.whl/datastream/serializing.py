import io
import struct
import typing

from datastream.base import BaseStream, ByteOrder


class SerializingStream(BaseStream):
    def __init__(
        self,
        buffer: typing.IO[bytes] | None = None,
        byteorder: int = ByteOrder.NATIVE_ENDIAN,
    ):
        if buffer is None:
            buffer = io.BytesIO()

        super().__init__(buffer, byteorder)

    def bytes(self) -> bytes:
        """
        Returns the bytes written to the stream.

        Returns:
            bytes: The bytes written to the stream.
        """
        return self._backing_stream.getvalue()

    def __bytes__(self) -> bytes: # type: ignore
        return self.bytes()

    def write_format(self, fmt: str, value: typing.Any):
        self.write(struct.pack(self._byteorder + fmt, value))

    def write_int64(self, value: int):
        self.write_format("q", value & 0x7FFFFFFFFFFFFFFF)

    def write_uint64(self, value: int):
        self.write_format("Q", value & 0xFFFFFFFFFFFFFFFF)

    def write_int32(self, value: int):
        self.write_format("i", value & 0x7FFFFFFF)

    def write_uint32(self, value: int):
        self.write_format("I", value & 0xFFFFFFFF)

    def write_int16(self, value: int):
        self.write_format("h", value & 0x7FFF)

    def write_uint16(self, value: int):
        self.write_format("H", value & 0xFFFF)

    def write_int8(self, value: int):
        self.write_format("b", value & 0x7F)

    def write_uint8(self, value: int):
        self.write_format("B", value & 0xFF)

    def write_float(self, value: float):
        self.write_format("f", value)

    def write_double(self, value: float):
        self.write_format("d", value)

    def write_bool(self, value: bool):
        self.write_uint8(int(value))

    def write_uleb128(self, value: int):
        """
        Writes a ULEB128(Unsigned Little-Endian Base 128) number to the data stream.
        This function does no bounds checking. It will encode the complete integer
        in `value` and write it to the stream.

        Parameters:
            value (int): The unsigned integer value to be written.
        """
        self.write_uleb128_safe(value, -1)

    def write_uleb128_safe(self, value: int, max_bytes: int = 16):
        """
        Writes a ULEB128(Unsigned Little-Endian Base 128) number to the data stream.

        Args:
            value (int): The unsigned integer value to be written.
            max_bytes (int, optional): The maximum number of bytes to use for encoding
                the value. Defaults to 16.
        """
        while max_bytes != 0:
            byte = value & 0x7F
            value >>= 7

            if value == 0:
                self.write_uint8(byte)

                break

            self.write_uint8(byte | 0x80)
            max_bytes -= 1

    def write_sleb128(self, value: int):
        """
        Writes a SLEB128(Signed Little-Endian Base 128) number to the data stream.
        This function does no bounds checking. It will encode the complete integer
        in `value` and write it to the stream.

        Parameters:
            value (int): The signed integer value to be written.
        """
        return self.write_sleb128_safe(value, -1)

    def write_sleb128_safe(self, value: int, max_bytes: int = 5):
        """
        Writes a SLEB128(Signed Little-Endian Base 128) number to the data stream.

        Args:
            value (int): The signed integer value to be written.
            max_bytes (int, optional): The maximum number of bytes to use for encoding
                the value. Defaults to 5.
        """
        if value >= 0:
            while max_bytes != 0 and value > 0x3F:
                self.write_uint8((value & 0x7F) | 0x80)

                # lsr >>> in java
                value %= 0x100000000
                value >>= 7

                max_bytes -= 1

            self.write_uint8(value & 0x7F)
        else:
            while max_bytes != 0 and value < -0x40:
                self.write_uint8((value & 0x7F) | 0x80)

                value >>= 7
                max_bytes -= 1

            self.write_uint8(value & 0x7F)
