# Datatype validator #

Utility module to validate common datatypes used by MantisTable, LamAPI and other projects.

Datatypes currently supported:

  * integer
  * real
  * boolean
  * string
  * date (various formats plus iso8601)
  * url
  * email
  * isbn (version 10 and 13)

Just import library and call get_datatype function

    import datatype
    data = datatype.get_datatype("34.2")
    print(data.is_valid())
    print(data.to_python())
    print(data.get_type())