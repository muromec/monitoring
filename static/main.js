function socket(dispatch) {
  const webSocket = new WebSocket(`ws://${location.host}/socket`);
  webSocket.onmessage = (event)=> {
    dispatch({type: 'UPDATED_PARAMS', data: JSON.parse(event.data)});
  };
  webSocket.onopen = ()=> {
    webSocket.send('START');
  };
  webSocket.onclose = ()=> {
  };
}

function reducer(state, {type, data}) {
  if (!state) {
    return {};
  }
  if (type === 'UPDATED_PARAMS') {
    return data;
  }

  return state;
}

function MonitoringBar({param, minValue, maxValue}, state) {
  const value = state[param];
  const percent = Math.max(
    Math.min(
      ((value - minValue) / (maxValue - minValue)) * 100,
      100),
    1
  );
  return {
    innerText: value.toFixed(2),
    style: {
      width: `${percent}%`,
    },
  };
}

const COMPONENTS = {
  '[data-param="ph"] div':
    MonitoringBar.bind(null, {param: 'ph', minValue: 4, maxValue: 7}),
  '[data-param="color"] div':
    MonitoringBar.bind(null, {param: 'color', minValue: 0, maxValue: 60}),
  '[data-param="bitterness"] div':
    MonitoringBar.bind(null, {param: 'bitterness', minValue: 0, maxValue: 80}),
  '[data-param="turbidity"] div':
    MonitoringBar.bind(null, {param: 'turbidity', minValue: 0, maxValue: 100}),
  '[data-param="alcohol"] div':
    MonitoringBar.bind(null, {param: 'alcohol', minValue: 0, maxValue: 20}),
  '[data-param="alcohol"] div':
    MonitoringBar.bind(null, {param: 'alcohol', minValue: 0, maxValue: 20}),
  '[data-param="attenuation"] div':
    MonitoringBar.bind(null, {param: 'attenuation', minValue: 0, maxValue: 100}),
  '[data-param="gravity"] div':
    MonitoringBar.bind(null, {param: 'gravity', minValue: 1, maxValue: 1.2}),
};


function updateAttributes(element, attributes) {
  Object.entries(attributes).forEach(([attribute, value])=> {
    if (value && typeof value === 'object') {
      updateAttributes(element[attribute], value);
    } else {
      element[attribute] = value;
    }
  });

}
function renderComponent(Component, element, state) {
  const result = Component(state);
  updateAttributes(element, Component(state));
}

function render(state) {
  Object.entries(COMPONENTS).forEach(([selector, Component])=> {
    const element = document.querySelector(selector);
    element && renderComponent(Component, element, state);
  });
}

function main() {
  let state = reducer(null, {type: 'INIT'});
  render(state);
  socket((action)=> {
    state = reducer(state, action);
    render(state);
  });
}

main()
