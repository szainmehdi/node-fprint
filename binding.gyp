{
	"targets": [
		{
			"target_name": "fingerprint",
			"sources": [ "src/enroll.cpp", "src/verify.cpp", "src/identify.cpp", "src/fingerprint.cpp" ],
			"include_dirs": [
				"<!(node -e \"require('nan')\")",
				"<!(pkg-config --cflags libfprint)",
				"<!(pkg-config --cflags zlib)"
			],
			"libraries": [
				"<!(pkg-config --libs libfprint)",
				"<!(pkg-config --libs-only-l zlib)"
			],
			"target_conditions": [
				[ "node_version == '0.10'", { "defines": ["OLD_UV_RUN_SIGNATURE"] } ]
			]
		}
	],
}
