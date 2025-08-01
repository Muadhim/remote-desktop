from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
import api

class AgentTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["ID", "Hostname", "OS", "Action"])
        self.load_agents()

    def load_agents(self):
        self.setRowCount(0)
        agents = api.get_agents()

        for row, agent in enumerate(agents):
            self.insertRow(row)
            self.setItem(row, 0, QTableWidgetItem(str(agent["id"])))
            self.setItem(row, 1, QTableWidgetItem(agent["hostname"]))
            self.setItem(row, 2, QTableWidgetItem(agent["os"]))

            delete_btn = QPushButton("Delete")
            delete_btn.clicked.connect(lambda _, a_id=agent["id"]: self.delete_agent(a_id))
            self.setCellWidget(row, 3, delete_btn)

    def delete_agent(self, agent_id):
        api.delete_agent(agent_id)
        self.load_agents()
