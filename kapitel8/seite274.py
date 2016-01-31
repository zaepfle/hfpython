# coding: utf-8
import android

app = android.Android()

app.dialogCreateAlert("Wählen Sie einen Sportler:")
app.dialogSetSingleChoiceItems(['Mark', 'Sarah', 'Ron', 'Julie'])
app.dialogSetPositiveButtonText("Wählen")
app.dialogSetNegativeButtonText("Beenden")
app.dialogShow()
antw = app.dialogGetResponse().result
