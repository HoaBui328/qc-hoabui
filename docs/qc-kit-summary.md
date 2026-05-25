# QC-Kit — Tóm tắt dự án

**Ngày tạo:** 2026-05-19  
**Tác giả:** QC Agent  
**Phiên bản:** v1

---

## 1. QC-Kit là gì?

QC-Kit là một framework tự động hóa QC (Quality Control) chạy trên Claude Code, chuẩn hóa quy trình kiểm thử chức năng từ đầu đến cuối: review yêu cầu → thiết kế kịch bản → sinh test case.

---

## 2. Dự án đang áp dụng

| Thông tin | Chi tiết |
|-----------|----------|
| Tên dự án | MBFS Mobile (Cục Đầu tư nước ngoài) |
| Nền tảng | Native iOS + Android |
| Quy mô | ~95 Use Cases, 6 modules, 64 màn hình |
| Trạng thái | Draft — đang triển khai |

---

## 3. Workflow chính

```
qc-project-onboarding
    → qc-context-master (tạo project-context-master.md)
        → qc-site-map (tạo site map 64 màn hình, 22 flows)
            → qc-dashboard-sync (đồng bộ dashboard 33 UC)
                → qc-uc-read (review từng UC)
                    → qc-func-scenario-design (thiết kế kịch bản test)
                        → qc-func-tc-design (sinh test case .md + .xlsx)
```

---

## 4. Skills đã triển khai (7 skills chính)

| Skill | Chức năng |
|-------|-----------|
| `qc-project-onboarding` | Khởi tạo project mới, cấu hình path-registry |
| `qc-context-master` | Tổng hợp kiến thức dự án thành 10 mục |
| `qc-site-map` | Bản đồ màn hình + luồng nghiệp vụ |
| `qc-dashboard-sync` | Quản lý trạng thái UC và artifact |
| `qc-uc-read` | Review UC, chấm điểm sẵn sàng, phát hiện gap |
| `qc-func-scenario-design` | Thiết kế test scenario từ UC đã review |
| `qc-func-tc-design` | Sinh test case chi tiết (.xlsx) |

---

## 5. Tiến độ hiện tại

### Dashboard (33 UC tracked)

- 20 UC: đã xác nhận In scope
- 13 UC: chờ xác nhận (Need confirm)
- Tất cả: chưa có file spec (đã bị clear ở commit trước)

### UC đã review

| UC | Tên | Kết quả | Điểm |
|----|-----|---------|------|
| UC1 | Home Dashboard | Conditionally Ready | 71.5/100 |
| UC45-51 | Quản lý hồ sơ | Conditionally Ready | 70.8/100 |
| UC256 | Đăng nhập Mobile | Ready | 77.7/100 |

### Test case đã sinh

| UC | Số lượng TC | Phiên bản |
|----|-------------|-----------|
| UC53_63-65 (Góp ý/Phản ánh) | 142 test cases | v1 (2026-05-14) |

---

## 6. Blockers & Vấn đề mở

### Blockers chính (Q-015)

- File spec trong `docs/ba/` và `docs/qc/` đã bị xóa — cần BA khôi phục
- Wireframe/mockup chưa có — block thiết kế test UI
- CMR_Mobile.md (Common Mobile Rules) chưa có — block scenario/TC design

### Câu hỏi chờ phản hồi

9/12 câu hỏi đang chờ BA/PM/Tech Lead trả lời (Q-002 → Q-012)

---

## 7. Cấu trúc thư mục

```
qc-kit/
├── .claude/
│   ├── config/path-registry.md    # Ánh xạ path cho tất cả artifact
│   ├── rules/                     # Quy tắc chung (ngôn ngữ, naming, etc.)
│   └── skills/                    # 7 skills QC + 3 utility skills
├── docs/
│   ├── ba/                        # File yêu cầu từ BA
│   ├── qc/                        # Output QC (review, scenario, TC)
│   └── qc-lead/                   # Dashboard, site-map, context, config
│       ├── project-config.md
│       ├── project-context-master.md
│       ├── qc-dashboard.md
│       ├── qc-site-map.md
│       ├── agent-work-log.md
│       └── high-level-files/      # WBS, Product Brief, Assumptions
├── guideline/                     # GitBook documentation
└── README.md
```

---

## 8. Nguyên tắc vận hành

- **Ngôn ngữ:** Output tiếng Việt, skill definition tiếng Anh
- **Versioning:** File không bao giờ bị ghi đè — tạo version mới (v1 → v2)
- **Evidence-based:** Mọi output phải trích dẫn nguồn cụ thể
- **Agent Work Log:** Mỗi lần chạy skill đều ghi log
- **Path Registry:** Tất cả path được quản lý tập trung, không hard-code

---

## 9. Modules của MBFS Mobile

| # | Module | Mô tả |
|---|--------|--------|
| 1 | Authentication | Đăng ký, đăng nhập, quên MK, OTP |
| 2 | Home | Dashboard, thông báo, tìm kiếm |
| 3 | Quản lý hồ sơ | Nộp/tra cứu/sửa hồ sơ đầu tư |
| 4 | Tra cứu KCN/KKT | Tìm kiếm khu công nghiệp, so sánh |
| 5 | Tin tức/Hỗ trợ | Tin tức, FAQ, góp ý, phản ánh |
| 6 | Thông báo | Push notification, lịch sử thông báo |
