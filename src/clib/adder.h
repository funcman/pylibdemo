#ifndef ADDER_H
#define ADDER_H

#ifdef _WIN32
    #define ADDER_API __declspec(dllexport)
#else
    #define ADDER_API
#endif

#ifdef __cplusplus
extern "C" {
#endif

ADDER_API int add(int a, int b);

#ifdef __cplusplus
}
#endif

#endif // ADDER_H 