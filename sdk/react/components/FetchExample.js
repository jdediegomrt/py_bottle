import React from 'react';
import { FlatList, StyleSheet, ActivityIndicator, Text, View, Button } from 'react-native';

export default class FetchExample extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isLoading: true };
  }

  componentDidMount() {
    return fetch('https://jdediegomrt-test.herokuapp.com/trivia/categories')
      .then(response => response.json())
      .then(responseJson => {
        this.setState(
          {
            isLoading: false,
            dataSource: responseJson.trivia_categories,
          },
          function() {}
        );
      })
      .catch(error => {
        console.error(error);
      });
  }

  render() {
    if (this.state.isLoading) {
      return (
        <View style={styles.container}>
          <ActivityIndicator />
        </View>
      );
    }

    return (
      <View style={styles.container}>
        <FlatList
          data={this.state.dataSource}
          renderItem={({ item }) => (
            <Button title={item.name.toString()}/>
          )}
          keyExtractor={item => item.id.toString()} 
        />
      </View>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    alignSelf: 'center',
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
