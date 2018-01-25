# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/DMT-git/src/ui/ui_proposals.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProposalsDlg(object):
    def setupUi(self, ProposalsDlg):
        ProposalsDlg.setObjectName("ProposalsDlg")
        ProposalsDlg.resize(932, 605)
        ProposalsDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProposalsDlg)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblMessage = QtWidgets.QLabel(ProposalsDlg)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout.addWidget(self.lblMessage)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnProposalsRefresh = QtWidgets.QPushButton(ProposalsDlg)
        self.btnProposalsRefresh.setAutoDefault(False)
        self.btnProposalsRefresh.setObjectName("btnProposalsRefresh")
        self.horizontalLayout.addWidget(self.btnProposalsRefresh)
        self.btnProposalsSaveToCSV = QtWidgets.QPushButton(ProposalsDlg)
        self.btnProposalsSaveToCSV.setAutoDefault(False)
        self.btnProposalsSaveToCSV.setObjectName("btnProposalsSaveToCSV")
        self.horizontalLayout.addWidget(self.btnProposalsSaveToCSV)
        self.btnProposalsColumns = QtWidgets.QPushButton(ProposalsDlg)
        self.btnProposalsColumns.setAutoDefault(False)
        self.btnProposalsColumns.setObjectName("btnProposalsColumns")
        self.horizontalLayout.addWidget(self.btnProposalsColumns)
        self.lblBudgetSummary = QtWidgets.QLabel(ProposalsDlg)
        self.lblBudgetSummary.setText("")
        self.lblBudgetSummary.setOpenExternalLinks(True)
        self.lblBudgetSummary.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblBudgetSummary.setObjectName("lblBudgetSummary")
        self.horizontalLayout.addWidget(self.lblBudgetSummary)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutFilter = QtWidgets.QHBoxLayout()
        self.layoutFilter.setObjectName("layoutFilter")
        self.lblProposalFilter = QtWidgets.QLabel(ProposalsDlg)
        self.lblProposalFilter.setObjectName("lblProposalFilter")
        self.layoutFilter.addWidget(self.lblProposalFilter)
        self.edtProposalFilter = QtWidgets.QLineEdit(ProposalsDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtProposalFilter.sizePolicy().hasHeightForWidth())
        self.edtProposalFilter.setSizePolicy(sizePolicy)
        self.edtProposalFilter.setMinimumSize(QtCore.QSize(300, 0))
        self.edtProposalFilter.setClearButtonEnabled(True)
        self.edtProposalFilter.setObjectName("edtProposalFilter")
        self.layoutFilter.addWidget(self.edtProposalFilter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.layoutFilter)
        self.detailsSplitter = QtWidgets.QSplitter(ProposalsDlg)
        self.detailsSplitter.setOrientation(QtCore.Qt.Vertical)
        self.detailsSplitter.setObjectName("detailsSplitter")
        self.propsView = QtWidgets.QTableView(self.detailsSplitter)
        self.propsView.setStyleSheet("QTableView{\n"
"  gridline-color: lightgray\n"
"}")
        self.propsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.propsView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.propsView.setAlternatingRowColors(False)
        self.propsView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.propsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.propsView.setShowGrid(True)
        self.propsView.setSortingEnabled(True)
        self.propsView.setObjectName("propsView")
        self.propsView.verticalHeader().setVisible(True)
        self.propsView.verticalHeader().setCascadingSectionResizes(False)
        self.propsView.verticalHeader().setHighlightSections(False)
        self.tabsDetails = QtWidgets.QTabWidget(self.detailsSplitter)
        self.tabsDetails.setObjectName("tabsDetails")
        self.tabDetails = QtWidgets.QWidget()
        self.tabDetails.setStyleSheet("")
        self.tabDetails.setObjectName("tabDetails")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabDetails)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.edtDetails = QtWidgets.QTextBrowser(self.tabDetails)
        self.edtDetails.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.edtDetails.setFrameShadow(QtWidgets.QFrame.Plain)
        self.edtDetails.setAcceptRichText(False)
        self.edtDetails.setOpenExternalLinks(True)
        self.edtDetails.setObjectName("edtDetails")
        self.verticalLayout_2.addWidget(self.edtDetails)
        self.tabsDetails.addTab(self.tabDetails, "")
        self.tabVoting = QtWidgets.QWidget()
        self.tabVoting.setObjectName("tabVoting")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabVoting)
        self.verticalLayout_5.setContentsMargins(5, 8, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollAreaVoting = QtWidgets.QScrollArea(self.tabVoting)
        self.scrollAreaVoting.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaVoting.setWidgetResizable(True)
        self.scrollAreaVoting.setObjectName("scrollAreaVoting")
        self.scrollAreaVotingContents = QtWidgets.QWidget()
        self.scrollAreaVotingContents.setGeometry(QtCore.QRect(0, 0, 409, 66))
        self.scrollAreaVotingContents.setObjectName("scrollAreaVotingContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaVotingContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layoutUserVoting = QtWidgets.QGridLayout()
        self.layoutUserVoting.setObjectName("layoutUserVoting")
        self.btnVoteNoForAll = QtWidgets.QPushButton(self.scrollAreaVotingContents)
        self.btnVoteNoForAll.setAutoDefault(False)
        self.btnVoteNoForAll.setObjectName("btnVoteNoForAll")
        self.layoutUserVoting.addWidget(self.btnVoteNoForAll, 0, 2, 1, 1)
        self.btnVoteAbstainForAll = QtWidgets.QPushButton(self.scrollAreaVotingContents)
        self.btnVoteAbstainForAll.setAutoDefault(False)
        self.btnVoteAbstainForAll.setObjectName("btnVoteAbstainForAll")
        self.layoutUserVoting.addWidget(self.btnVoteAbstainForAll, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaVotingContents)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.layoutUserVoting.addWidget(self.label_3, 0, 0, 1, 1)
        self.btnVoteYesForAll = QtWidgets.QPushButton(self.scrollAreaVotingContents)
        self.btnVoteYesForAll.setAutoDefault(False)
        self.btnVoteYesForAll.setObjectName("btnVoteYesForAll")
        self.layoutUserVoting.addWidget(self.btnVoteYesForAll, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaVotingContents)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.layoutUserVoting.addWidget(self.label_4, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutUserVoting.addItem(spacerItem2, 0, 5, 1, 1)
        self.verticalLayout_3.addLayout(self.layoutUserVoting)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.scrollAreaVoting.setWidget(self.scrollAreaVotingContents)
        self.verticalLayout_5.addWidget(self.scrollAreaVoting)
        self.tabsDetails.addTab(self.tabVoting, "")
        self.tabVoteList = QtWidgets.QWidget()
        self.tabVoteList.setObjectName("tabVoteList")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabVoteList)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.votesSplitter = QtWidgets.QSplitter(self.tabVoteList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.votesSplitter.sizePolicy().hasHeightForWidth())
        self.votesSplitter.setSizePolicy(sizePolicy)
        self.votesSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.votesSplitter.setObjectName("votesSplitter")
        self.layoutWidget = QtWidgets.QWidget(self.votesSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutVotesView = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layoutVotesView.setContentsMargins(0, 0, 0, 0)
        self.layoutVotesView.setSpacing(2)
        self.layoutVotesView.setObjectName("layoutVotesView")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnVotesRefresh = QtWidgets.QPushButton(self.layoutWidget)
        self.btnVotesRefresh.setAutoDefault(False)
        self.btnVotesRefresh.setObjectName("btnVotesRefresh")
        self.horizontalLayout_2.addWidget(self.btnVotesRefresh)
        self.btnVotesSaveToCSV = QtWidgets.QPushButton(self.layoutWidget)
        self.btnVotesSaveToCSV.setAutoDefault(False)
        self.btnVotesSaveToCSV.setObjectName("btnVotesSaveToCSV")
        self.horizontalLayout_2.addWidget(self.btnVotesSaveToCSV)
        self.chbOnlyMyVotes = QtWidgets.QCheckBox(self.layoutWidget)
        self.chbOnlyMyVotes.setToolTip("")
        self.chbOnlyMyVotes.setObjectName("chbOnlyMyVotes")
        self.horizontalLayout_2.addWidget(self.chbOnlyMyVotes)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.layoutVotesView.addLayout(self.horizontalLayout_2)
        self.layoutVotesViewFilter = QtWidgets.QHBoxLayout()
        self.layoutVotesViewFilter.setSpacing(8)
        self.layoutVotesViewFilter.setObjectName("layoutVotesViewFilter")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.layoutVotesViewFilter.addWidget(self.label_2)
        self.edtVotesViewFilter = QtWidgets.QLineEdit(self.layoutWidget)
        self.edtVotesViewFilter.setObjectName("edtVotesViewFilter")
        self.layoutVotesViewFilter.addWidget(self.edtVotesViewFilter)
        self.btnApplyVotesViewFilter = QtWidgets.QPushButton(self.layoutWidget)
        self.btnApplyVotesViewFilter.setAutoDefault(False)
        self.btnApplyVotesViewFilter.setObjectName("btnApplyVotesViewFilter")
        self.layoutVotesViewFilter.addWidget(self.btnApplyVotesViewFilter)
        self.layoutVotesView.addLayout(self.layoutVotesViewFilter)
        self.votesView = QtWidgets.QTableView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.votesView.sizePolicy().hasHeightForWidth())
        self.votesView.setSizePolicy(sizePolicy)
        self.votesView.setObjectName("votesView")
        self.votesView.verticalHeader().setVisible(False)
        self.layoutVotesView.addWidget(self.votesView)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.votesSplitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layoutVotesChart = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutVotesChart.setContentsMargins(0, 0, 0, 0)
        self.layoutVotesChart.setObjectName("layoutVotesChart")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rbVotesChartIncremental = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbVotesChartIncremental.setChecked(True)
        self.rbVotesChartIncremental.setObjectName("rbVotesChartIncremental")
        self.horizontalLayout_3.addWidget(self.rbVotesChartIncremental)
        self.rbVotesChartFinal = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbVotesChartFinal.setObjectName("rbVotesChartFinal")
        self.horizontalLayout_3.addWidget(self.rbVotesChartFinal)
        self.rbVotesChartChanges = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbVotesChartChanges.setObjectName("rbVotesChartChanges")
        self.horizontalLayout_3.addWidget(self.rbVotesChartChanges)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.layoutVotesChart.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.votesSplitter)
        self.tabsDetails.addTab(self.tabVoteList, "")
        self.verticalLayout.addWidget(self.detailsSplitter)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProposalsDlg)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProposalsDlg)
        self.tabsDetails.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProposalsDlg)

    def retranslateUi(self, ProposalsDlg):
        _translate = QtCore.QCoreApplication.translate
        ProposalsDlg.setWindowTitle(_translate("ProposalsDlg", "Dialog"))
        self.btnProposalsRefresh.setText(_translate("ProposalsDlg", "Refresh"))
        self.btnProposalsSaveToCSV.setText(_translate("ProposalsDlg", "Save to CSV..."))
        self.btnProposalsColumns.setText(_translate("ProposalsDlg", "Columns..."))
        self.lblProposalFilter.setText(_translate("ProposalsDlg", "Filter"))
        self.edtProposalFilter.setPlaceholderText(_translate("ProposalsDlg", "proposal name / title / owner"))
        self.tabsDetails.setTabText(self.tabsDetails.indexOf(self.tabDetails), _translate("ProposalsDlg", "Details"))
        self.btnVoteNoForAll.setToolTip(_translate("ProposalsDlg", "Vote No for all masternodes."))
        self.btnVoteNoForAll.setText(_translate("ProposalsDlg", "No For All"))
        self.btnVoteAbstainForAll.setToolTip(_translate("ProposalsDlg", "Vote Abstain for all masternodes."))
        self.btnVoteAbstainForAll.setText(_translate("ProposalsDlg", "Abstain For All"))
        self.btnVoteYesForAll.setToolTip(_translate("ProposalsDlg", "Vote Yes for all masternodes."))
        self.btnVoteYesForAll.setText(_translate("ProposalsDlg", "Yes For All"))
        self.tabsDetails.setTabText(self.tabsDetails.indexOf(self.tabVoting), _translate("ProposalsDlg", "Vote"))
        self.btnVotesRefresh.setToolTip(_translate("ProposalsDlg", "Reads new votes from the Dash network"))
        self.btnVotesRefresh.setText(_translate("ProposalsDlg", "Refresh"))
        self.btnVotesSaveToCSV.setText(_translate("ProposalsDlg", "Save to CSV..."))
        self.chbOnlyMyVotes.setText(_translate("ProposalsDlg", "Show my votes only"))
        self.label_2.setText(_translate("ProposalsDlg", "Filter:"))
        self.btnApplyVotesViewFilter.setText(_translate("ProposalsDlg", "Apply"))
        self.rbVotesChartIncremental.setText(_translate("ProposalsDlg", "Votes by date (incremental)"))
        self.rbVotesChartFinal.setText(_translate("ProposalsDlg", "Votes summary"))
        self.rbVotesChartChanges.setText(_translate("ProposalsDlg", "Vote changes by date"))
        self.tabsDetails.setTabText(self.tabsDetails.indexOf(self.tabVoteList), _translate("ProposalsDlg", "Voting History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProposalsDlg = QtWidgets.QDialog()
    ui = Ui_ProposalsDlg()
    ui.setupUi(ProposalsDlg)
    ProposalsDlg.show()
    sys.exit(app.exec_())

