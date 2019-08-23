import * as React from 'react';
import Layout from './components/layout';

interface Iprops {

}
interface Istate {

}

export default class App extends React.Component<Iprops, Istate>{
  constructor(props: string | number | object | Function ) {
    super(props)
  }
  render() {
    return (
      <div>
        <Layout></Layout>
      </div>
    )
  }
}