import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import FetchExample from './components/FetchExample'
import ErrorBoundary from 'react-native-error-boundary'

export default function App() {
  return (
    <ErrorBoundary>
      <View style={styles.container}>
        <FetchExample></FetchExample>
      </View>
    </ErrorBoundary>
  );
}

const CustomFallback = (props) => (
  <View>
    <Text>Something happened!</Text>
    <Text>{props.error.toString()}</Text>
    <Button onPress={props.resetError} title={'Try again'} />
  </View>
)

const errorHandler = (error, stackTrace) => {
  /* Log the error to an error reporting service */
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
