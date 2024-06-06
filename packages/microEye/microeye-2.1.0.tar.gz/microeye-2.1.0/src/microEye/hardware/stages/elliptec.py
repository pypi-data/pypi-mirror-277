from microEye.hardware.port_config import port_config
from microEye.qt import QtCore, QtSerialPort, QtWidgets


class elliptec_controller:
    '''Thorlabs Elliptec stage controller'''

    def __init__(self) -> None:
        self._connect_btn = QtWidgets.QPushButton()

        self.serial = QtSerialPort.QSerialPort(None, readyRead=self.rx_piezo)
        self.serial.setBaudRate(9600)
        self.serial.setPortName('COM9')

    def isOpen(self):
        '''Returns True if connected.'''
        return self.serial.isOpen()

    def open(self):
        '''Opens the serial port.'''
        self.serial.open(QtCore.QIODevice.OpenModeFlag.ReadWrite)

    def close(self):
        '''Closes the supplied serial port.'''
        self.serial.close()

    def setPortName(self, name: str):
        '''Sets the serial port name.'''
        self.serial.setPortName(name)

    def setBaudRate(self, baudRate: int):
        '''Sets the serial port baudrate.'''
        self.serial.setBaudRate(baudRate)

    def open_dialog(self):
        '''Opens a port config dialog
        for the serial port.
        '''
        dialog = port_config(
            baudrate=self.serial.baudRate(), portname=self.serial.portName()
        )
        if not self.isOpen():
            if dialog.exec():
                portname, baudrate = dialog.get_results()
                self.setPortName(portname)
                self.setBaudRate(baudrate)

    def write(self, value):
        self.serial.write(value)

    def HOME(self, address):
        '''Homes the stage at a specific address'''
        if self.isOpen():
            self.LastCmd = f'{address}ho0'
            self.write(self.LastCmd.encode('utf-8'))

    def FORWARD(self, address):
        '''Moves the stage at a specific address one step FORWARD'''
        if self.isOpen():
            self.LastCmd = f'{address}fw'
            self.write(self.LastCmd.encode('utf-8'))

    def BACKWARD(self, address):
        '''Moves the stage at a specific address one step BACKWARD'''
        if self.isOpen():
            self.LastCmd = f'{address}bw'
            self.write(self.LastCmd.encode('utf-8'))

    def setSLOT(self, address, slot):
        '''Moves the stage at a specific address one step BACKWARD'''
        if self.isOpen():
            self.LastCmd = f'{address}ma000000{slot * 2}0'
            self.write(self.LastCmd.encode('utf-8'))

    def rx_piezo(self):
        '''Controller dataReady signal.'''
        self.Received = str(self.serial.readAll(), encoding='utf8')

    def getQWidget(self):
        '''Generates a QGroupBox with
        stage controls.'''
        group = QtWidgets.QGroupBox('Elliptec Controller')
        layout = QtWidgets.QFormLayout()
        group.setLayout(layout)

        self._connect_btn = QtWidgets.QPushButton(
            'Connect', clicked=lambda: self.open()
        )
        self._disconnect_btn = QtWidgets.QPushButton(
            'Disconnect', clicked=lambda: self.close()
        )
        self._config_btn = QtWidgets.QPushButton(
            'Config.', clicked=lambda: self.open_dialog()
        )

        btns = QtWidgets.QHBoxLayout()
        btns.addWidget(self._connect_btn)
        btns.addWidget(self._disconnect_btn)
        btns.addWidget(self._config_btn)
        layout.addRow(btns)

        self.address_bx = QtWidgets.QSpinBox()
        self.address_bx.setMinimum(0)
        self.address_bx.setMaximum(9)

        layout.addRow(QtWidgets.QLabel('Address:'), self.address_bx)

        self.stage_type = QtWidgets.QComboBox()
        self.stage_type.addItems(['ELL6', 'ELL9'])

        layout.addRow(QtWidgets.QLabel('Stage Type:'), self.stage_type)

        self._add_btn = QtWidgets.QPushButton(
            'Add stage',
            clicked=lambda: self.add_stage(
                self.stage_type.currentText(), self.address_bx.value(), layout
            ),
        )

        layout.addWidget(self._add_btn)

        return group

    def add_stage(self, stage_type, address, layout):
        if 'ELL6' in stage_type:
            self.getELL6(address, layout)
        elif 'ELL9' in stage_type:
            self.getELL9(address, layout)

    def getELL6(self, address, layout: QtWidgets.QFormLayout):
        group = QtWidgets.QGroupBox(f'Ell6 (2 SLOTS) Address {address}')
        move_buttons = QtWidgets.QHBoxLayout()
        group.setLayout(move_buttons)
        # controls
        HOME_btn = QtWidgets.QPushButton('⌂', clicked=lambda: self.HOME(address))
        BW_btn = QtWidgets.QPushButton('<<', clicked=lambda: self.BACKWARD(address))
        FW_btn = QtWidgets.QPushButton('>>', clicked=lambda: self.FORWARD(address))
        remove_btn = QtWidgets.QPushButton('x', clicked=lambda: layout.removeRow(group))

        move_buttons.addWidget(HOME_btn)
        move_buttons.addWidget(BW_btn)
        move_buttons.addWidget(FW_btn)
        move_buttons.addWidget(remove_btn)

        group.button_group = QtWidgets.QButtonGroup()
        group.button_group.setExclusive(True)
        group.button_group.addButton(BW_btn)
        group.button_group.addButton(FW_btn)

        FW_btn.setCheckable(True)
        BW_btn.setCheckable(True)

        layout.addRow(group)

    def getELL9(self, address, layout: QtWidgets.QFormLayout):
        group = QtWidgets.QGroupBox(f'Ell9 (4 SLOTS) Address {address}')
        move_buttons = QtWidgets.QHBoxLayout()
        group.setLayout(move_buttons)
        # controls
        HOME_btn = QtWidgets.QPushButton('⌂', clicked=lambda: self.HOME(address))
        BW_btn = QtWidgets.QPushButton('<<', clicked=lambda: self.BACKWARD(address))
        FW_btn = QtWidgets.QPushButton('>>', clicked=lambda: self.FORWARD(address))
        remove_btn = QtWidgets.QPushButton('x', clicked=lambda: layout.removeRow(group))
        first_btn = QtWidgets.QPushButton(
            '1st', clicked=lambda: self.setSLOT(address, 0)
        )
        second_btn = QtWidgets.QPushButton(
            '2nd', clicked=lambda: self.setSLOT(address, 1)
        )
        third_btn = QtWidgets.QPushButton(
            '3rd', clicked=lambda: self.setSLOT(address, 2)
        )
        fourth_btn = QtWidgets.QPushButton(
            '4th', clicked=lambda: self.setSLOT(address, 3)
        )

        move_buttons.addWidget(HOME_btn)
        move_buttons.addWidget(BW_btn)
        move_buttons.addWidget(FW_btn)
        move_buttons.addWidget(first_btn)
        move_buttons.addWidget(second_btn)
        move_buttons.addWidget(third_btn)
        move_buttons.addWidget(fourth_btn)
        move_buttons.addWidget(remove_btn)

        group.button_group = QtWidgets.QButtonGroup()
        group.button_group.setExclusive(True)
        group.button_group.addButton(first_btn)
        group.button_group.addButton(second_btn)
        group.button_group.addButton(third_btn)
        group.button_group.addButton(fourth_btn)

        first_btn.setCheckable(True)
        second_btn.setCheckable(True)
        third_btn.setCheckable(True)
        fourth_btn.setCheckable(True)

        layout.addRow(group)
