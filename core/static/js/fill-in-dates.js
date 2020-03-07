/* requires moment */

const dateCells = document.querySelectorAll('.date')
const initLength = dateCells.length
const dataHolder = document.querySelector('#data-holder')
const habitPK = dataHolder.dataset.pk


if (initLength > 1) {
  const firstDate = moment(dateCells[0].textContent, 'MMMM D, YYYY')
  const lastDate = moment(dateCells[initLength - 1].textContent, 'MMMM D, YYYY')

  // let day = firstDate.clone()

  for (let day = firstDate; day.isAfter(lastDate); day.subtract(1, 'days')) {
    const prevDay = day.clone()
    prevDay.add(1, 'days')
    const dateString = day.format('MMMM D, YYYY')
    // console.log(dateString)
    const cell = document.querySelector(`[data-date='${dateString}']`)
    if (cell == null) {
      addRow(prevDay, day)
    }
  }
}
else {
  const titleRow = document.querySelector('tr')
  const rowBelow = document.createElement('tr')
  rowBelow.innerHTML = `<td></td><td class="achievement"><a href="/add-log?habit=${habitPK}">Add a log</a></td>`
  titleRow.insertAdjacentElement('afterend', rowBelow)
}

function addRow (prevDay, day) {
  const prevDayString = prevDay.format('MMMM D, YYYY')
  const dayString = day.format('MMMM D, YYYY')
  const urlDayString = day.format('YYYY-MM-DD')

  const rowAbove = document.querySelector(`[data-date='${prevDayString}']`).closest('tr')
  const rowBelow = document.createElement('tr')
  rowBelow.innerHTML = `<td class="date" data-date="${dayString}">${dayString}</td>
  <td class="achievement"><a href="/add-log?habit=${habitPK}&date=${urlDayString}">Add a log</a></td>`
  rowAbove.insertAdjacentElement('afterend', rowBelow)
}