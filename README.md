# WebGL API

This API surfaces data for use in the WebGL visualization. 

Results are returned in JSON. The general format is:

```json
[key, [[lat, lon, magnitude], ..., [lat, lon, magnitude]]
```

Example request for 10 fires with magnitude coming from the brightness column:

[http://ecohackfirez.appspot.com/api/webgl?count=10&mag=brightness](http://ecohackfirez.appspot.com/api/webgl?count=13&mag=brightness)

Result:

```json
[
  [
    "04/16/2012",
    [
      28.914999999999999,
      19.780999999999999,
      306.5
    ]
  ],
  [
    "04/16/2012",
    [
      21.864000000000001,
      98.677000000000007,
      319.80000000000001
    ]
  ],
  [
    "04/16/2012",
    [
      11.105,
      -6.3369999999999997,
      332.80000000000001
    ]
  ]
]
```

Description of URL parameters:

<table>
    <tr>
        <td><b>Parameter</b></td>
        <td><b>Description</b></td>
        <td><b>Example</b></td>
    </tr>
    <tr>
        <td>count</td>
        <td>Number of fires to return</td>
        <td>10</td>
    </tr>
    <tr>
        <td>mag</td>
        <td>Magnitude of fire (brightness or confidence)</td>
        <td>confidence</td>
    </tr>
</table>

