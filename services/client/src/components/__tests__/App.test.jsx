import React from 'react';
import { shallow } from 'enzyme';

import App from '../../App';

test('App renders withour crashing', () => {
    const wrapper = shallow(<App/>);
});
